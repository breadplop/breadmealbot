import telebot
import parser
import bs4

TOKEN = '457069682:AAE--jQfpX_M_QfYd3s1pN_3yXbKvT1-Zzk'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['start', 'breakfast', 'dinner', 'today'])

def start_handler(message):
    bot.send_message(message.chat.id, "Type 'today' or 'tomorrow' \
    sorry my functions are limited as of today....")
    

@ bot.message_handler (content_types = ['text'])
def text_handler (message):
    text = message.text.lower ()
    chat_id = message.chat.id
    if text == "today":
        bot.send_message (chat_id, 'todays menu is')
    elif text == "tomorrow":
        bot.send_message (chat_id, 'tmr menu is')
    else:
        bot.send_message (chat_id, '**Sorry, I did not understand :(** unbolded')

@ bot.message_handler (content_types = ['photo'])
def text_handler (message):
    chat_id = message.chat.id
    bot.send_message (chat_id, 'Beautiful.')
bot.polling()