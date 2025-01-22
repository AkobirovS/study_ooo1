from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

operater = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="+"),KeyboardButton(text="-")],
        [KeyboardButton(text="*"),KeyboardButton(text="/")],
        [KeyboardButton(text="**")]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)