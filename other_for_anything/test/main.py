# # def multiply(self, num1: str, num2: str) -> str:
# #     if num1.isnumeric() and num2.isnumeric():
# #         num1 = int(num1)
# #         num2 = int(num2)
# #         return str(num1 * num2)
# #     else:
# #         return "type errore"
#
#
# def merge(intervals: list[list[int]]):
#     if len(intervals) > 1 :
#         sorted(intervals)
#         intervals[0][1] = intervals[1][1]
#         del intervals[1]
#         return intervals
#     else:
#         return intervals
#
# print(merge([[1,3],[2,6],[8,10],[15,18]]))



import asyncio
import logging
from aiogram.filters.state import State, StatesGroup
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html , F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
import buttons as b
# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()

class User(StatesGroup):
    number_1 = State()
    number_2 = State()
    operater = State()
@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await message.answer(f"Assalom Alykum , {message.from_user.full_name} welcome my calculater!")
    await message.answer(f"add the first number")
    await state.set_state(User.number_1)

@dp.message(User.number_1)
async def add_the_number_1(message: Message, state: FSMContext):
    if message.text.isnumeric():
        await state.update_data(number_1=message.text)
        await message.answer("Add the second number")
        await state.set_state(User.number_2)
    else:
        await message.answer("Add a number, please!")

@dp.message(User.number_2)
async def add_the_number_2(message: Message, state: FSMContext):
    if message.text.isnumeric():
        await state.update_data(number_2=message.text)
        await message.answer("Numbers are saved!",reply_markup=b.operater)
        await state.set_state(User.operater)
        # Здесь можно добавить логику для дальнейших операций
    else:
        await message.answer("Add a number, please!")

@dp.message(User.operater)
async def add_the_number_2(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == "+":
        number = int(data["number_1"]) + int(data["number_2"])
        await message.answer(f"{number}")
    elif message.text == "-":
        number = int(data["number_1"]) - int(data["number_2"])
        await message.answer(f"{number}")
    elif message.text == "*":
        number = int(data["number_1"]) * int(data["number_2"])
        await message.answer(f"{number}")
    elif message.text == "/":
        number = int(data["number_1"]) / int(data["number_2"])
        await message.answer(f"{number}")
    elif message.text == "**":
        number = int(data["number_1"]) ** int(data["number_2"])
        await message.answer(f"{number}")
    else:
        await message.answer("erore")
    await state.clear()
    # if message.text.isnumeric():
    #     await state.update_data(number_2=message.text)
    #     await message.answer("add the second number",reply_markup=b.operater)
    #     await state.set_state(User.operater)
    # else:
    #     await message.answer("add the number please !!!")
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())