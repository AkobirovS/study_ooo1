import aiogram
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joi kerak")
        ],
        [
            KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")
        ],
        [KeyboardButton(text="Shogird kerak")]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="please use the bot to your goodness !!!!!!!!!"
)

get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Add the number !!!",request_contact=True)]],
    one_time_keyboard=True,
    resize_keyboard=True
)

get_the_onswer = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="ha"),KeyboardButton(text="yo'q")]],
    one_time_keyboard=True,
    resize_keyboard=True
)
get_the_admin_answer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="ha",callback_data="ha"),
        InlineKeyboardButton(text="yo'q",callback_data="no")
    ]]
)