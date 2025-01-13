import logging
from logging import basicConfig

from aiogram import Bot,Dispatcher,executor ,types

API_TOKEN = ""

logging,basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message(command="start")
async def start(message: types.Message):
    await bot.send_message(message.chat.id, message.text)