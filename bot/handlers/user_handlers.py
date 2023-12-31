from pprint import pprint
from random import randint
from datetime import date

from aiogram import types, Dispatcher

from bot.keyboards.user_keyboards import get_main_kb, get_years_kb, get_start_kb
from bot.storage import storage


async def cmd_start(msg: types.Message) -> None:
    """Command start
    """
    global storage
    storage = {}
    reply_text1 = f'Привет, {msg.from_user.first_name}\n'
    reply_text2 = 'Выбери год'

    await msg.answer(text=reply_text1,reply_markup=get_start_kb())
    await msg.answer(text=reply_text2, reply_markup=get_years_kb())


def register_user_handlers(dp: Dispatcher) -> None:
    """Register user handlers
    """

    dp.register_message_handler(cmd_start, commands=['start'])
