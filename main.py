import peeweedbevolve
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from bot import MQBot
from config import TG_TOKEN, DB, IS_DEBUG
from handlers.conversation import main_menu, button
from handlers.sample import start
from jobs.sample import broadcast_job
from models import debug_create_tables


def db_migrate():
    if not IS_DEBUG:
        peeweedbevolve.evolve(DB, interactive=False, ignore_tables=['basemodel'])
    else:
        debug_create_tables()


def bot_run():
    # TODO::CREATE setup logging

    bot = MQBot(TG_TOKEN)
    updater = Updater(bot=bot, workers=4, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^Main menu$'), main_menu))
    dp.add_handler(CallbackQueryHandler(button, pattern='button\d'))

    updater.job_queue.run_repeating(broadcast_job, interval=60, first=0)

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    db_migrate()
    bot_run()
