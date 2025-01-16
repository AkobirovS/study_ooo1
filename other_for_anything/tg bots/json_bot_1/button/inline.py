from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startBTN = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="? savol bormi ?"),KeyboardButton(text="! vazifa jo'natish !")]
    ],
    resize_keyboard=True,
    input_field_placeholder="hello to my bot ..."
)
start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="? savol bormi ?"),KeyboardButton(text="! vazifa jo'natish !")]
    ],
    resize_keyboard=True,
    input_field_placeholder="hello to my bot ...",
    one_time_keyboard=True
)

group = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="331"), KeyboardButton(text="775")],
        [KeyboardButton(text="556"),KeyboardButton(text="977")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="add the number !!!" ,request_contact= True,)]],
    resize_keyboard= True
)