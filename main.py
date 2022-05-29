import os

import telebot
from number import check_number
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name} Что бы получить ссылку для отправки сообщения в WhatsApp без добавления в список контактов, просто пришлите номер:'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    text = message.text
    number, flag = check_number(text)
    if not flag:
        bot.send_message(message.chat.id, f"https://api.whatsapp.com/send?phone={number}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "В номере не может быть букв")
    bot.send_message(message.chat.id,
                     "Что бы получить ссылку для отправки сообщения в WhatsApp без добавления в список контактов, просто пришлите номер:")


bot.polling(none_stop=True)