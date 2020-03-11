from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize
import settings
from clarifai.rest import ClarifaiApp
import pprint

def get_user_emo(user_data):
    if 'emo' not in user_data:
        emo = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        user_data['emo'] = emo
        return user_data['emo']


def get_keyboard():
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Send your location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Send cat','Change avatar'],[contact_button, location_button]])
    return my_keyboard

def get_avatar(user_data):
    emo = get_user_emo(user_data)
    return emo

#функция ищущая кошку
def is_cat(file_name):
    image_has_cat = False
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    response = model.predict_by_filename(file_name, max_concepts=5)
    if response['status']['code'] == 10000:
        for concept in response['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                image_has_cat = True
    return image_has_cat
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(response)


def check_user_photo(bot, update, user_data):
    update.message.reply_text("Обрабатываю фото")
    os.makedirs('downloads', exist_ok=True)
    photo_file = bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', '{}.jpg'.format(photo_file.file_id))
    photo_file.download(filename)
    if is_cat(filename):
        update.message.reply_text("Обнаружен котик, добавляю в библиотеку.")
        new_filename = os.path.join('images', 'cat_{}.jpg'.format(photo_file.file_id))
        os.rename(filename, new_filename)
    else:
        os.remove(filename)
        update.message.reply_text("Тревога, котик не обнаружен!")


if __name__ == "__main__":
    print(is_cat('images/cat1.jpg'))