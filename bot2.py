#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from load_data import tdy, tmr, load_data, format_menu
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

data = load_data()

def start(bot, update):
    keyboard = [[InlineKeyboardButton("Today's Menu", callback_data='today'),
                 InlineKeyboardButton("Tomorrow's Menu", callback_data='tomorrow')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    if query.data == 'today':
        bot.edit_message_text(
                        text='*TODAY\'S MENU:* \n' + format_menu(data[tdy]),
                        parse_mode=ParseMode.MARKDOWN,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    elif query.data == 'tomorrow':
        bot.edit_message_text(
                        text='*TOMORROW\'S MENU:* \n' + format_menu(data[tmr]),
                        parse_mode=ParseMode.MARKDOWN,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    else:    
        bot.sendmessage(query.message.chat_id,"dunno??")

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ.get('TOKEN'))

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()