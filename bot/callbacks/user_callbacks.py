from random import randint
from aiogram.dispatcher.filters import Text

from datetime import date, timedelta
from babel.dates import format_date
from aiogram import Dispatcher, types
from bot.storage import storage
from bot.keyboards.user_keyboards import get_month_kb, get_day_kb, get_period_kb

async def cb_year(call: types.CallbackQuery):
    storage['year'] = int(call.data.split(':')[1])
    reply_text = f'Выбран год: {storage["year"]}\n'
    reply_text+='Выбери месяц'
    await call.message.answer(text=reply_text, reply_markup=get_month_kb())


async def cb_month(call: types.CallbackQuery):
    storage['month'] = int(call.data.split(':')[1])
    reply_text = f'Выбран год: {storage["year"]}\n'
    reply_text += f'Выбран месяц: {storage["month"]}\n'
    reply_text += 'Выбери день'
    await call.message.answer(text=reply_text, reply_markup=get_day_kb())


async def cb_day(call: types.CallbackQuery):
    storage['day'] = int(call.data.split(':')[1])
    reply_text = f'Выбран год: {storage["year"]}\n'
    reply_text += f'Выбран месяц: {storage["month"]}\n'
    reply_text += f'Выбран день: {storage["day"]}\n'
    reply_text += 'Выберете период'
    await call.message.answer(text=reply_text, reply_markup=get_period_kb())


async def cb_period(call: types.CallbackQuery):
    storage['period'] = int(call.data.split(':')[1])

    d = date(storage['year'], storage['month'], storage['day'])
    date_of_purchase = d - timedelta(days=storage['period']-1)
    date_of_purchase = format_date(date_of_purchase, locale='ru', format='dd MMMM YYYY')
    d = format_date(d,locale='ru', format='dd MMMM YYYY')
    reply_text = f'Продажа на {d} открывается {date_of_purchase} (за {storage["period"]} дней)'
    await call.message.answer(text=reply_text)


def register_user_callbacks(dp: Dispatcher) -> None:
    """Register user callbacks
    """

    dp.register_callback_query_handler(cb_year, Text(startswith='year:'))
    dp.register_callback_query_handler(cb_month, Text(startswith='month:'))
    dp.register_callback_query_handler(cb_day, Text(startswith='day:'))
    dp.register_callback_query_handler(cb_period, Text(startswith='period:'))