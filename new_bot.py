import telebot
import random
import requests

from telebot import types

bot = telebot.TeleBot("1421596613:AAGML7ko_1aOPpaNufIXQtU0FFIpU7xh0A0")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #Кнопки выбора
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📝 Тесты")
    item2 = types.KeyboardButton("Определения 🔑")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом. В дальнейшем, я буду помогать операторам в подготовке к экзменам!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '📝 Тесты':
            bot.send_message(message.chat.id, "Тесты скоро тут появятся")
        elif message.text == "Определения 🔑":

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Написать ", callback_data='good')
        

            markup.add(item1)
        
            bot.send_message(message.chat.id, "Ок", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')





bot.polling()