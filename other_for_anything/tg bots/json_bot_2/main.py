# import logging
#
# from aiogram import Bot, Dispatcher,types
# import asyncio
#
# API_TOKEN = "8045172020:AAGhrFzWqAci6TwDCK7RBLTxeNAJysQ5mIQ"
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=["strat"])
# async def start_command(message: types.Message):
#     await message.reply("Hello!")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
import json
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '8045172020:AAGhrFzWqAci6TwDCK7RBLTxeNAJysQ5mIQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['s']))
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum!\nSizga qanday yordam bera o laman?")

@dp.message(Command(commands=["hello"]))
async def feply_hello(message: types.Message):
    await bot.send_message(chat_id=5412637724, text="hello oo ")

@dp.message()
async def echo(message: types.Message):
    user = 5412637724

    await message.answer(message.text)
    await bot.send_message(chat_id=user,text=f"""
    vam ot {message.chat.full_name} eto {message.text}
    """)

    await bot.send_message(chat_id=user, text="Sardorkhon")

    jsonss = json.loads(message)

    print(jsonss)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
