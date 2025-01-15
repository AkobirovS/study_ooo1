import asyncio
from aiogram import Bot , Dispatcher

from app.handlers import router


async def main():
    Tokens = "8045172020:AAHDYFc2tqXJB78Pse1yP6qyOJDvc5duApI"
    bot = Bot(Tokens)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("bot turn off !")


