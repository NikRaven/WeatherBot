import telebot
import requests
import json

bot = telebot.TeleBot('6835483986:AAF8jPjuSa_c9smAM_sqH7rNobfrAxRoO4U')
API = '02d19f2ce58652c8e5e9dd56b1b9d758'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши в каком городе ты бы хотел знать погоду!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        #print(data["weather"][0]["main"])   достаём погодные условия
        bot.reply_to(message, f'Сейчас температура: {data["main"]["temp"]}')

        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан неверно!')


bot.polling(none_stop=True)  # программа постоянно работает