# импорт компонентов, обработчика команд, обработчик текстовых сообщений(1,2), фильтр, кнопка с текстом 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton  # Импорт модуля разметки клавиатуры, получение геолокации и конт. данных пользователя
from settings import *
from utils import *
from handlers import *

# Настройки прокси
PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"}}

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler(["start", "hello"],  greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler("^(Прислать котика)$", send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
