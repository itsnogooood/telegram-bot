import telebot
from telebot import types
from man_to_woman import zodiac_signs, man_list
from woman_to_man import woman_list


bot = telebot.TeleBot('1396114943:AAE5RcR6Grkb0to-UytMtjv9udP1NynFA8c')


@bot.message_handler(commands=['help'])
def start_message(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, 'yo, you have done /help')


@bot.message_handler(commands=['start'])
def male(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        item1 = types.KeyboardButton('Male')
        item2 = types.KeyboardButton('Female')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Choose your male', reply_markup=markup)
        if message.text == 'Male':
            man_list_bot = man_list
        elif message.text == 'Female':
            woman_list_bot = woman_list


@bot.message_handler(commands=['Male', 'Female'])
def first_sign(message):
    if message.text in 'Male' or 'Female':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        item1 = zodiac_signs[0]
        item2 = zodiac_signs[1]
        item3 = zodiac_signs[2]
        item4 = zodiac_signs[3]
        item5 = zodiac_signs[4]
        item6 = zodiac_signs[5]
        item7 = zodiac_signs[6]
        item8 = zodiac_signs[7]
        item9 = zodiac_signs[8]
        item10 = zodiac_signs[9]
        item11 = zodiac_signs[10]
        item12 = zodiac_signs[11]
        markup.row(item1, item2, item3, item4)
        markup.row(item5, item6, item7, item8)
        markup.row(item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Choose first sign ', reply_markup=markup)


@bot.message_handler(commands=[zodiac_signs])
def second_sing(message):
    if message.text in zodiac_signs:
        bot.send_message(message.chat.id, 'EEEE')

bot.polling()
