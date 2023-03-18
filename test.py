import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


api_token = '6152168622:AAH0hk668cuzuMw79JSDnE2owzuwLKlh09I'
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()
    password = State()

@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!\nWelcom to CoddyCoinKepper_bot!")

@dp.message_handler(Command("enter"))
async def autorization(message: types.Message):
    await message.answer("Введите логин")
    await Form.name.set()
@dp.message_handler(state=Form.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    data = await state.get_data()
    con = sqlite3.connect("CoddyCoinKepeer.db")
    cursor = con.cursor()
    user_info = cursor.execute("select * from admins where name like '%" + data['username'] + "%'").fetchall()
    if len(user_info) > 0:
        await message.answer("Логин принят! Введите пароль.")
        await Form.next()
    else:
        await message.answer("Пользователя с таким логином не существует")
@dp.message_handler(state=Form.password)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(userpass=message.text)
    data = await state.get_data()
    con = sqlite3.connect("CoddyCoinKepeer.db")
    cursor = con.cursor()
    user_info = cursor.execute("select * from admins where pass like '%" + data['userpass'] + "%'").fetchall()
    if len(user_info) > 0:
        await message.answer("Пароль принят.")
        await state.finish()
    else:
        await message.answer("Неверный пароль.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
