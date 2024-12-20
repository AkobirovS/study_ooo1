# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
#
#
# # Функция для обработки команды /start
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Привет! Я твой бот.')
#
#
# # Функция для обработки команды /help
# def help(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Напиши /start, чтобы получить приветственное сообщение.')
#
#
# def main():
#     # Используй свой токен
#     TOKEN = 'YOUR_BOT_TOKEN'
#
#     # Создаём объект Updater с токеном бота
#     updater = Updater(TOKEN)
#
#     # Получаем диспетчера для регистрации обработчиков
#     dispatcher = updater.dispatcher
#
#     # Регистрируем обработчики команд
#     dispatcher.add_handler(CommandHandler('start', start))
#     dispatcher.add_handler(CommandHandler('help', help))
#
#     # Начинаем получать обновления от Telegram
#     updater.start_polling()
#
#     # Ожидаем завершения работы
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()
# #
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import PicklePersistence


# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Используй команду /get_tokens, чтобы получить токены.")


# Функция для получения случайного количества токенов
def get_tokens(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Получаем текущие токены пользователя из хранилища
    user_data = context.bot_data.get(user_id, {'tokens': 0})

    # Генерируем случайное количество токенов (от 1 до 10)
    tokens_earned = random.randint(1, 10)
    user_data['tokens'] += tokens_earned

    # Сохраняем обновленное количество токенов
    context.bot_data[user_id] = user_data

    update.message.reply_text(f"Ты получил {tokens_earned} токенов! У тебя теперь {user_data['tokens']} токенов.")


# Функция для отображения текущего баланса токенов
def check_balance(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_data = context.bot_data.get(user_id, {'tokens': 0})
    update.message.reply_text(f"У тебя на балансе {user_data['tokens']} токенов.")


def main():
    # Токен бота
    TOKEN = 'YOUR_BOT_TOKEN'

    # Настройка хранилища для данных бота
    persistence = PicklePersistence("bot_data.pkl")

    # Создаем объект Updater с токеном и хранилищем
    updater = Updater(TOKEN, persistence=persistence)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('get_tokens', get_tokens))
    dispatcher.add_handler(CommandHandler('balance', check_balance))

    # Начинаем получать обновления
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()


if __name__ == '__main__':
    main()
