import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from aiogram import types
import sqlite3

api_token = '6152168622:AAH0hk668cuzuMw79JSDnE2owzuwLKlh09I'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token)
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message_handler(Command("pp"))
async def get_smt(message: types.Message):
    await message.answer("Введите имя")
@dp.callback_query_handler(Command("admin"))
async def auth_admin(call: types.CallbackQuery):
    # await call.answer(cache_time=5)
    await call.message.answer('Введите Логин:')
    # await authorization_admins.login.set()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

