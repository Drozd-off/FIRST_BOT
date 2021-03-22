
"""  Modul for start bot   """

from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters
from constants import API_TOKEN
from functions import *


updater = Updater(token=API_TOKEN, )

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',
                                      start))

dispatcher.add_handler(MessageHandler(Filters.text,
                                      text_msg))

updater.start_polling()
