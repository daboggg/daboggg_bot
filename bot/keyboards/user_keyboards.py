from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import date
from bot.storage import storage


def get_start_kb()-> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/start'))


def get_main_kb() -> InlineKeyboardMarkup:
    """Get kb for main menu
    """
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Число от 1 до 10', callback_data='random'),
            InlineKeyboardButton('Число от 10 до 100', callback_data='random1'),
        ]
    ])

    return ikb


def get_years_kb() -> InlineKeyboardMarkup:
    """Get years kb
    """
    current_year = date.today().year
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(str(current_year), callback_data='year:' + str(current_year)),
            InlineKeyboardButton(str(current_year + 1), callback_data='year:' + str(current_year + 1)),
        ]
    ], resize_keyboard=True)

    return ikb


def get_month_kb()->InlineKeyboardMarkup:

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(str(m), callback_data='month:' + str(m)) for m in range(1,5)],
        [InlineKeyboardButton(str(m), callback_data='month:' + str(m)) for m in range(5,9)],
        [InlineKeyboardButton(str(m), callback_data='month:' + str(m)) for m in range(9,13)]
    ], resize_keyboard=True)


def get_day_kb()->InlineKeyboardMarkup:
    year = int(storage['year'])
    month = int(storage['month'])

    daysInMonth = 0
    if month == 2: daysInMonth = 29 if year % 4 == 0 else 28
    if month in [1,3,5,7,8,10,12]: daysInMonth = 31
    if month in [4,6,9,11]: daysInMonth = 30

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(str(m), callback_data='day:' + str(m)) for m in range(1,8)],
        [InlineKeyboardButton(str(m), callback_data='day:' + str(m)) for m in range(8,15)],
        [InlineKeyboardButton(str(m), callback_data='day:' + str(m)) for m in range(15,22)],
        [InlineKeyboardButton(str(m), callback_data='day:' + str(m)) for m in range(22,29)],
        [InlineKeyboardButton(str(m), callback_data='day:' + str(m)) for m in range(29,daysInMonth + 1)],
    ], resize_keyboard=True)


def get_period_kb()->InlineKeyboardMarkup:

    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('45', callback_data='period:45'),
            InlineKeyboardButton('60', callback_data='period:60'),
            InlineKeyboardButton('90', callback_data='period:90'),
        ]
    ], resize_keyboard=True)
