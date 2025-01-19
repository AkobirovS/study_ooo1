import asyncio
import logging
import sys
import os
from email.policy import default
from idlelib.undo import Command
from lib2to3.fixes.fix_input import context
from lib2to3.pgen2.tokenize import group
from os import getenv
from turtledemo.clock import datum

from aiogram.filters.state import State ,StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Contact, CallbackQuery
import buttons as b
# Bot token can be obtained via https://t.me/BotFather

# TOKEN = os.getenv("BOT_TOKEN")
TOKEN = "8045172020:AAHDYFc2tqXJB78Pse1yP6qyOJDvc5duApI"
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

class User(StatesGroup):
    name = State()
    tex = State()
    number = State()
    gel = State()
    dollor = State()
    job = State()
    work_time = State()
    goat = State()
    group = State()
    answer = State()
    think_admin = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message,state: FSMContext) -> None:
    await message.answer(f"Assalom Alykum , {message.from_user.full_name}!",reply_markup=b.start_buttons)
    await state.set_state(User.group)


@dp.message(Command("help"))
async def hello(message:Message,state: FSMContext):
    await message.answer("hrll")

@dp.message(User.group)
async def sherik(message: Message, state: FSMContext):
    await state.update_data(group=message.text)
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(User.name)


@dp.message(User.name)
async def add_the_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan,

Java, C++, C#""")
    await state.set_state(User.tex)


@dp.message(User.tex)
async def get_naviks(message: Message, state:FSMContext):
    text = message.text.split(",")
    await state.update_data(tex=text)

    await message.answer("""📞 Aloqa:

    Bog`lanish uchun raqamingizni kiriting?
    Masalan, +998 90 123 45 67 yoku add qiling """,reply_markup=b.get_number)
    await state.set_state(User.number)


@dp.message(User.number)
async def add_the_number(message:Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    await message.answer("""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")

    await state.set_state(User.gel)

@dp.message(User.gel)
async def add_the_gel(message:Message, state: FSMContext):
    await state.update_data(gel=message.text)
    await message.answer("""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await state.set_state(User.dollor)

@dp.message(User.dollor)
async def dollor(message: Message, state:FSMContext):
    await state.update_data(dollor=message.text)
    await message.answer("""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await state.set_state(User.job)

@dp.message(User.job)
async def get_job(message:Message,state:FSMContext):
    await state.update_data(job=message.text)
    await message.answer("""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(User.work_time)

@dp.message(User.work_time)
async def goat(message:Message,state: FSMContext):
    await state.update_data(work_time=message.text)

    await message.answer("""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.""")

    await state.set_state(User.goat)

@dp.message(User.goat)
async def chaking(message:Message, state:FSMContext):
    await state.update_data(goat=message.text)
    data = await state.get_data()
    await message.answer(f"""{data['group']}:
🏅 {data['group']}:  {data["name"]}
📚 Texnologiya: {data["tex"]}
🇺🇿 Telegram: {message.chat.full_name}
📞 Aloqa: {data['number']}
🌐 Hudud: {data["gel"]}
💰 Narxi: {data['dollor']}
👨🏻‍💻 Kasbi: {data['job']}
🕰 Murojaat qilish vaqti: {data['work_time']}    
🔎 Maqsad: {data['goat']}""")
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=b.get_the_onswer)
    await state.set_state(User.answer)

@dp.message(User.answer)
async def chakking(message:Message,state:FSMContext):
    await state.update_data(answer=message.text)
    data = await state.get_data()
    if data["answer"] == "ha":
        await message.bot.send_message(chat_id=5412637724, text=f"""{data['group']}:
🏅 {data['group']}:  {data["name"]}
📚 Texnologiya: {data["tex"]}
🇺🇿 Telegram: {message.chat.full_name}
📞 Aloqa: {data['number']}
🌐 Hudud: {data["gel"]}
💰 Narxi: {data['dollor']}
👨🏻‍💻 Kasbi: {data['job']}
🕰 Murojaat qilish vaqti: {data['work_time']}    
🔎 Maqsad: {data['goat']}""",reply_markup=b.get_the_admin_answer)
    elif data["answer"] == "yo'q":
        await message.answer("try again")
    else:
        await message.answer("errore try again")

@dp.callback_query(F.data == "ha")
async def answer_the_think(call:CallbackQuery):
    await call.message.answer("hello")



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())