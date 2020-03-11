from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize
import settings
from utils import get_user_emo, get_keyboard
from glob import glob # команда отсылающая картинку

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data["emo"] = emo
    text = "Привет {}".format(emo)
    #my_keyboard = ReplyKeyboardMarkup([["/cat"]])
    update.message.reply_text(text, reply_markup=my_keyboard)

    # функция которая будет "отвечать" пользователю
def talk_to_me(bot, update, user_data):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

# ищет файты в папке  с названием catpip install python-telegram-bot[socks] emoji
glob("images/*cat*.jp*g")

# функция которая отсылает картинку
def send_cat_picture(bot, update, user_data):
    cat_list = glob("images/*cat*.jp*g")
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, "rb"))


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text("Спасибо {}".format(get_avatar(user_data)))


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text("Спасибо {}".format(get_avatar(user_data)))


def change_avatar(bot, update, user_data):
    # if 'emo' in user_data:
    #     del user_data['emo']
    user_data.pop('emo', None)
    emo = get_user_emo(user_data)
    update.message.reply_text("Avatar has changed! {}".format(emo),reply_markup=get_keyboard())