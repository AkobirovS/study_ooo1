from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton

startBTN = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="? savol bormi ?"),KeyboardButton(text="! vazifa jo'natish !")]
    ],
    resize_keyboard=True,
    input_field_placeholder="hello to my bot ...",
    one_time_keyboard=True
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

marks_button = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="1",callback_data="1-ball"),
        InlineKeyboardButton(text="2",callback_data="2-ball"),
        InlineKeyboardButton(text="3",callback_data="3-ball"),
        InlineKeyboardButton(text="4",callback_data="4-ball"),
        InlineKeyboardButton(text="5",callback_data="5-ball")
    ],
    [
        InlineKeyboardButton(text="6", callback_data="6-ball"),
        InlineKeyboardButton(text="7", callback_data="7-ball"),
        InlineKeyboardButton(text="8", callback_data="8-ball"),
        InlineKeyboardButton(text="9", callback_data="9-ball"),
        InlineKeyboardButton(text="10", callback_data="10-ball")]],
    resize_keyboard=True,
    one_time_keyboard=True
)