from random import choice

import markovify
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.error import BadRequest
from db_phrases import add_phrase, get_random_phrase


def create_text_model(update, context):
    with open("full.txt", "r", encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.Text(text)
    context.user_data['model'] = text_model
    return 

def greet_user(update, context):
    create_text_model(update, context)
    text = f'Приветствую, уважаемый {update.message.chat.first_name}! Присоединяйся к дружине тюменских журналистов на фронтах спортивных баталий! Просто отправь мне «Вперед»'
    return update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())
    
def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup(
        [['Добавить'], ['Пропустить']],
        resize_keyboard=True
        )
    return my_keyboard    

def learning(update, context):
    if update.message.text == 'Пропустить':
        context.user_data['ph'] = None
    check = context.user_data.get('ph')
    if check:
        add_phrase(check)
    new_phrase = context.user_data['model'].make_sentence()
    edited_new_phrase = new_phrase.replace('.', '. ').replace(".  ", ". ")
    context.user_data['ph'] = edited_new_phrase
    try:
        update.message.reply_text(edited_new_phrase, reply_markup=get_keyboard())
    except BadRequest:
        update.message.reply_text(edited_new_phrase, reply_markup=get_keyboard())

def get_phrase(update, context):
    phrase = get_random_phrase()

    return update.message.reply_text(phrase)
