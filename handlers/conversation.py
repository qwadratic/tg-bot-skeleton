from random import randint

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from models import User


def get_scoring(address):
    return randint(1, 100)


def button(update: Update, ctx: CallbackContext):
    q = update.callback_query
    data = q.data
    button_number = data[-1]
    q.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('new text' if button_number == '1' else 'button1', callback_data='button1'),
            InlineKeyboardButton('new text' if button_number == '2' else 'button2', callback_data='button2')
        ],
            [InlineKeyboardButton(str(get_scoring('address')), url='https://google.com')]
        ]))
    q.answer('ok, {}'.format(data))


def main_menu(update: Update, ctx: CallbackContext):
    u, is_created = User.get_or_create(
        tg_id=update.message.from_user.id,
        defaults={
            'username': update.message.from_user.username
        })
    msg = "This is menu with inline buttons"
    ctx.bot.send_message(u.tg_id, msg, reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('button 1', callback_data='button1'),
            InlineKeyboardButton('button 2', callback_data='button2')
        ],
            [InlineKeyboardButton(str(get_scoring('address')), url='https://google.com')]
        ]
    ))

