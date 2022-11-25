# pip freeze >requirements.txt    - создание файла со списком всех библиотек текущего окружения.

# 22 ноября, тема Телеграмм-бот.

# Взаимодействие с ботом происходит через переменную bot (токен надо вставить свой).
# Декоратор @message_handler реагирует на входящие сообщение.
# Message – это объект из Bot API, содержащий в себе информацию о сообщении. Полезные поля:
# message.chat.id – идентификатор чата
# message.from.id – идентификатор пользователя
# message.text – текст сообщения
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.

import telebot
import json


API_TOKEN='5925350659:AAHpjfR8i-gah2l02XABQTsMSpDfBt2sSSU'

bot = telebot.TeleBot(API_TOKEN)

calc = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")

films=['Мортал комбат', "Матрица"]
@bot.message_handler(commands=['show'])
def show_message(message):
    bot.send_message(message.chat.id, ''.join(films))

@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    #eq = message.text.split()[1:]
    #print(eq[0])
    #print(eval(eq[0]))
    calc=True
    bot.send_message(message.chat.id,'А теперь введите выражение для расчета')    

@bot.message_handler(content_types='text')
def check_message(message):
    global calc
    if 'привет' in message.text:
        bot.send_message(message.chat.id,'И тебе привет коли не шутишь!')  
    if calc:
         calc=False
         bot.send_message(message.chat.id,'результат равен '+str(eval(message.text)))


bot.polling()