#импорт компонентов для бота в телеге,подписка на обработчик команд, обработчик текстовых сообщений
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройки прокси
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

#отчет о работе
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

#Тело бота Teleg
def main():
    mybot = Updater("1101438743:AAEhudeGnN6YR-XbvkxC87soncerAReH9m4", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

#функция ответа пользователю
def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)



#ОТВЕТ БОТА
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

#запуск
main()
