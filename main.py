import peeweedbevolve
from telegram.ext import Updater

from bot import MQBot
from config import TG_TOKEN, DB, IS_DEBUG
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

    # TODO::CREATE add handlers and jobs

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    db_migrate()
    bot_run()
