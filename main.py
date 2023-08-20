import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.handlers.user_handlers import register_user_handlers
from bot.callbacks.user_callbacks import register_user_callbacks


def register_handler(dp: Dispatcher) -> None:
    register_user_handlers(dp)

def register_callback(dp: Dispatcher) -> None:
    register_user_callbacks(dp)


async def main() -> None:
    """Entry point
    """
    load_dotenv('.env')
    token = os.getenv('TOKEN_API')
    bot = Bot(token)
    dp = Dispatcher(bot)

    register_handler(dp)
    register_callback(dp)

    try:
        await dp.start_polling()
        logging.info('start')
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == '__main__':
    asyncio.run(main())
