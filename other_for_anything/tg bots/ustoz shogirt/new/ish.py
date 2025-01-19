from aiogram import F,Router
from aiogram.types import Message
dp = Router()

@dp.message(F.text == "Ish joyi kerak")
async def need_job(message:Message):
    await message.answer("kjdgsfkjadgs")
