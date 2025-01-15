from aiogram import F , Router
from aiogram.types import Message , CallbackQuery
from aiogram.filters import CommandStart , Command
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(CommandStart())
async def cmd(message: Message):
    await message.answer("hello and welcome to our Fast food bot!!!\nand the other news /help", reply_markup=kb.main)


@router.message(Command("help"))
async def cmd_main(message: Message):
    await message.reply("if you want to answer anything\ncall at this number please :) ! (:\nthank you for time")


@router.message(F.text == "Catalog")
async def cmd(message: Message):
    await message.reply("chose one of the foods!!!", reply_markup=kb.catalog)

@router.callback_query(F.data == "Fs-Food")
async def call_back(callback_data: CallbackQuery):
    await callback_data.answer("you chose the fast food",show_alert=True)

@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Add the your name please (:")

@router.message(Register.name)
async def register_mane(message: Message, state: FSMContext):
    await  state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Add the your age please (:")

@router.message(Register.age)
async def register_age(message: Message, state : FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Add the your number please (:",reply_markup=kb.get_number)

@router.message(Register.number,F.contact)
async def register_number(message:Message,state:FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"your name: {data['name']}\nyour age is {data['age']}\nyour number is {data['number']}")
    await state.clear()


@router.message(F.text == "number")
async def number(message: Message):
    await message.answer("add your number", reply_markup=kb.get_number)
