from telebot import types, TeleBot
from os import environ
from glob import iglob
from data import DataForLibrary
from database import Library
from datetime import datetime


token = environ.get('API_Token')
bot = TeleBot(token)
admin_id = environ.get('Admin_chat_id')


@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_message = f'Вітаю, {message.from_user.first_name}! Ти завітав до нашої бібліотеки 📔.\n' \
                      f'/category - список усіх категорій\n/feedback - зворотній звя\'зок\n/help - список усіх команд'
    date_now = datetime.utcfromtimestamp(int(message.date)).strftime('%d-%m-%Y %H:%M:%S')
    try:
        if Library().check_user(message.chat.id) is None:
            Library().add_user(message.chat.id, message.chat.first_name, message.chat.last_name,
                               message.chat.username, date_now)
    except Exception as e:
        try:
            Library().add_error(message.chat.id, str(e), date_now)
        except Exception as e:
            bot.send_message(admin_id, str(e))
    list_user_info = [str(message.chat.id), str(message.chat.first_name), str(message.chat.last_name),
                      str(message.chat.username)]
    str_user_info = ' '.join(list_user_info)
    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(commands=['help'])
def helper(message):
    helper_message = '/start - стартова сторінка\n/category - список усіх категорій\n/feedback - зворотній звя\'зок'
    bot.send_message(message.chat.id, helper_message)


@bot.message_handler(commands=['category'])
def category(message):
    keyboard = types.InlineKeyboardMarkup()
    all_categories = DataForLibrary().categories('books')
    for category in all_categories:
        try:
            category_button = types.InlineKeyboardButton(text=category, callback_data=category)
            keyboard.add(category_button)
        except Exception as e:
            try:
                date_now = datetime.utcfromtimestamp(int(message.date)).strftime('%d-%m-%Y %H:%M:%S')
                Library().add_error(message.chat.id, str(e), date_now)
            except Exception as e:
                bot.send_message(admin_id, str(e))
    bot.send_message(message.chat.id, 'Перелік усіх категорій:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.endswith('book'))
def callback_books(call):
    call_data_dict = DataForLibrary().split_call_data(call.data)
    category = call_data_dict[0]
    books_dict = DataForLibrary().dict_with_books('books/%s' % category)
    book_name = books_dict[int(call_data_dict[1])]
    date_now = datetime.utcfromtimestamp(int(call.message.date)).strftime('%d-%m-%Y %H:%M:%S')
    try:
        for file in iglob(f'books/{category}/{book_name}/*'):
            with open(f'{file}', 'rb') as f:
                bot.send_document(call.message.chat.id, f)
    except Exception:
        bot.send_message(call.message.chat.id, 'Щось пішло не так, спробуй ще.')
    try:
        Library().add_action(call.message.chat.id, str(book_name), date_now)
    except Exception as e:
        try:
            Library().add_error(call.message.chat.id, str(e), date_now)
        except Exception as e:
            bot.send_message(admin_id, str(e))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    all_categories = DataForLibrary().categories('books')
    if call.data in all_categories:
        books_dict = DataForLibrary().dict_with_books('books/%s' % call.data)
        keyboard = types.InlineKeyboardMarkup()
        for book in books_dict:
            try:
                button_book = types.InlineKeyboardButton(text=books_dict[book],
                                                         callback_data=f'{call.data}/{book}/book')
                keyboard.add(button_book)
            except Exception as e:
                try:
                    date_now = datetime.utcfromtimestamp(int(call.message.date)).strftime('%d-%m-%Y %H:%M:%S')
                    Library().add_error(call.message.chat.id, str(e), date_now)
                except Exception as e:
                    bot.send_message(admin_id, str(e))
        bot.send_message(call.message.chat.id, 'Перелік книжок \n/category - до списку категорій',
                         reply_markup=keyboard)


@bot.message_handler(commands=['feedback'])
def category(message):
    bot.send_message(message.chat.id, 'Що Ви хочете нам сказати?')
    bot.register_next_step_handler(message, feedback)


@bot.message_handler(content_types=['text'])
def any_text(message):
    bot.send_message(message.chat.id, 'Я тебе не розумію.\n/help - список усіх команд')


def feedback(message):
    date_now = datetime.utcfromtimestamp(int(message.date)).strftime('%d-%m-%Y %H:%M:%S')
    try:
        Library().add_feedback(message.chat.id, message.text, date_now)
    except Exception as e:
        try:
            Library().add_error(message.chat.id, str(e), date_now)
        except Exception as e:
            bot.send_message(admin_id, str(e))
    list_user_info = [date_now, str(message.chat.id), str(message.chat.first_name), str(message.chat.last_name),
                      str(message.chat.username), str(message.text)]
    str_user_info = ' '.join(list_user_info)
    bot.send_message(admin_id, str_user_info)
    bot.send_message(message.chat.id, 'Дякуємо за Ваш Зворотній зв\'язок!\n/start - стартова сторінка')


bot.polling()
