#импорт компонентов, обработчика команд, обработчик текстовых сообщений(1,2),
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from glob import glob  # команда отсылающая картинку
from random import choice
from emoji import emojize #импорт эмоджи 
from telegram import ReplyKeyboardMarkup, KeyboardButton # Импорт модуля разметки клавиатуры, получение геолокации и конт. данных пользователя 
import settings


TOKEN = "1101438743:AAEhudeGnN6YR-XbvkxC87soncerAReH9m4"

# Настройки прокси
PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"}}

#ищет файты в папке  с названием cat
glob('images/*cat*.jp*g')

def greet_user(bot, update):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет  {}'.format(emo)
    my_keyboard = ReplyKeyboardMarkup([['/cat']])
    update.message.reply_text(text, reply_markup=my_keyboard)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))  # команда /cat
    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    mybot.start_polling()
    mybot.idle()

#функция с клавиатурой
def get_keyboard():
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Send your location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Send cat','Change avatar'],[contact_button, location_button]])

#функция которая отсылает картинку
def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/*cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


#функция которая будет "отвечать" пользователю
def talk_to_me(bot, update, user_data):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Спасибо {}'.format(get_avatar(user_data)))

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Спасибо {}'.format(get_avatar(user_data)))

main()
