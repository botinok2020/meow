import logging
import sqlite3
import asyncio
from avito import datall
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types.message import Message
from aiogram.filters.command import CommandStart, Command

#bebe = []
#bebe = datall()

router = Router()
bot = Bot(token='7858030157:AAEqohD-traSjCoVj1wxlgwv1MOy4lRDULU')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello")

@dp.message(Command('all_data'))
async def really(message: Message):
    await bot.send_message(message.from_user.id, datall())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")