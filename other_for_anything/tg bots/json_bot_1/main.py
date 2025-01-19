import asyncio
import logging
import sys
from email.policy import default
from os import getenv
from symtable import Class
from tkinter.font import names

# from dotev import load_dotev

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart , Command
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from pyexpat.errors import messages

# load_dotev()

from button import inline as m
from button.inline import group

TOKEN = "8045172020:AAHDYFc2tqXJB78Pse1yP6qyOJDvc5duApI"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()



class User(StatesGroup):
    name = State()
    number = State()
    file = State()
    description = State()
    groups = State()




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Assalom Alyekum\nxush kelibsiz bizning vazifa botimizga\n\nBuyerda siz uzuzni uyga vazifalaringizni yuborasiz !!!\n/help ", reply_markup=m.startBTN)

@dp.message(F.text == "? savol bormi ?")
async def qustion_hendler(message: Message):
    await message.answer("Barch savolaringizga turu ustozga murojat\nqilsangiz tushunishingiz yaxsh bo'ladi !")

@dp.message(F.text == "! vazifa jo'natish !")
async def add_the_groups(message: Message,state: FSMContext):
    await message.reply("vazifani jonatish uchun kerakli malumotlar olish kerak",reply_markup=m.group)
    await state.set_state(User.groups)


@dp.message(User.groups)
async def add_the_name(message: Message, state:FSMContext):
    the_aswer = message.text
    await state.update_data(groups=the_aswer)
    await message.answer("ismizni kiriting")
    await state.set_state(User.name)

@dp.message(User.name)
async def add_the_name(message:Message, state:FSMContext):
    the_answer = message.text
    await state.update_data(name=the_answer)
    await message.answer("add the number !!!", reply_markup=m.get_number)
    await state.set_state(User.number)

@dp.message(User.number,F.contact)
async def add_the_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    await message.answer("add the description ! ")
    await state.set_state(User.description)

@dp.message(User.description)
async def add_the_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("add the your file")
    await state.set_state(User.file)

@dp.message(User.file)
async def add_the_file(message: Message, state: FSMContext):
    print(message.document.file_id)
    await state.update_data(file=message.document.file_id)
    data = await state.get_data()
    await message.bot.send_document(chat_id=5412637724, document=message.document.file_id, caption=f"""
    🆔 User Id: {message.chat.id}
    👤 User: <em>{data['name']}</em>
    📫 Group: <i>{data['groups']}</i>
    📞 Phone: +{data['number']}
    🔍 Username: @{message.from_user.username}
    📃 description: <b>{data['description']}</b>
    """, parse_mode='html', reply_markup=m.marks_button)

    await message.answer("your task will be check",reply_markup=m.start)
    await state.clear()


# @dp.callback_query(lambda call: call.data in [f"{i}-ball" for i in range(1,11)])
# async def ball_hendler(call: CallbackQuery):
#
#     print(call)



@dp.callback_query(lambda call: call.data in [f"{i}-ball" for i in range(1, 11)])
async def ball_handler(call: CallbackQuery,state: FSMContext):
    # Ensure `call.message` and its attributes exist
    if not call.message or not call.message.caption:
        await call.answer("Error: Message or caption missing.", show_alert=True)
        return

    # Extract the chat ID from the caption (assuming a fixed slice is valid)
    chat_id = call.message.caption[11:21]

    # Send the document to the extracted chat ID
    await call.message.bot.send_document(
        chat_id=int(chat_id),
        document=call.message.document.file_id,
        caption=f"Ustoz sizning ushbu vazifangizni <b><i>{call.data}</i></b> bilan baholadilar!",
        parse_mode='HTML'
    )

    # Delete the original message
    await call.message.delete()

    # Send the document to a fixed recipient
    await call.message.bot.send_document(
        chat_id=949677905,
        document=call.message.document.file_id,
        caption=f"""{call.message.caption}

<b><i>{call.data}</i></b> bilan baholandi """,
        parse_mode='HTML'
    )

    # Acknowledge the callback query
    await call.answer("Message sent successfully!", show_alert=True)
    await state.clear()



# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")
#

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("bot turn off !")