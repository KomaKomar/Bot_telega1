#импорт компонентов, обработчика команд, обработчик текстовых сообщений(1,2),
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from glob import glob  # команда отсылающая картинку
from random import choice
from emoji import emojize #импорт эмоджи 
import settings


TOKEN = "1101438743:AAEhudeGnN6YR-XbvkxC87soncerAReH9m4"

# Настройки прокси
PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"}}

#ищет файты в папке  с названием cat
glob('images/*cat*.jp*g')



def greet_user(bot, update):
    smile = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    text = 'Привет {}'.format(smile)
    update.message.reply_text(text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cat", send_cat_picture))  # команда /cat
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


#функция которая отсылает картинку
def send_cat_picture(bot, update):
    cat_list = glob('images/*cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


#функция которая будет "отвечать" пользователю
def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


main()
