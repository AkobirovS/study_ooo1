from idlelib.editor import keynames

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Trash")],
    [KeyboardButton(text="Catalog")],
    [
        KeyboardButton(text="Contect"),
        KeyboardButton(text="about us")
    ]],
resize_keyboard = True,
input_field_placeholder="what the foot do you want..."
)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="fast Food",callback_data="Fs-Food")],
    [InlineKeyboardButton(text="Nation's foods", callback_data="Nash-Food")],
    [InlineKeyboardButton(text="Sneak", callback_data="Snaek"),InlineKeyboardButton(text="sodas",callback_data="Soda")]])

get_number= ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Do add the number ?",request_contact=True)]],
                                resize_keyboard=True)