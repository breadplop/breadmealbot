import telebot
from load_data import tdy, tmr, load_data, format_menu
import telegram
from extra_functions import menu, button_list
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)
data = load_data()
#button_menu = menu

@bot.message_handler(commands = ['start', 'breakfast', 'dinner', 'today'])
def start_handler(message):
    bot.send_message(message.chat.id, "Type 'today' or 'tomorrow' \
    \n sorry my functions are limited as of today....")
    #reply_markup = telegram.ReplyKeyboardMarkup(button_menu)
    #bot.send_message(..., "A two-column menu", reply_markup=reply_markup)
    start_markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    start_markup_btn1 = telebot.types.KeyboardButton('/start')
    start_markup.add(start_markup_btn1)

    source_markup = telebot.types.ReplyKeyboardMarkup (row_width = 2, resize_keyboard = True)
    source_markup_btn1 = telebot.types.KeyboardButton ('smart-topics')
    source_markup_btn2 = telebot.types.KeyboardButton ('webdeveloper-topics')
    source_markup.add (source_markup_btn1, source_markup_btn2)
    

@ bot.message_handler (content_types = ['text'])
def text_handler (message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "today":
        bot.send_message(chat_id, '*TODAY\'S MENU:* \n' + \
        format_menu(data[tdy]),parse_mode=telegram.ParseMode.MARKDOWN)
    elif text == "tomorrow":
        bot.send_message (chat_id, '*TOMORROW\'S MENU:* \n' + \
        format_menu(data[tmr]),parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.send_message (chat_id, '*Sorry, I did not understand :(* unbolded',parse_mode=telegram.ParseMode.MARKDOWN)
        bot.send_message (chat_id, '_italics_ ',parse_mode=telegram.ParseMode.MARKDOWN)

bot.polling()

