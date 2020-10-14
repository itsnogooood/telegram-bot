import telebot
from telebot import types
from man_to_woman import zodiac_signs
from settings import key
from back import choose_male

bot = telebot.TeleBot(key)


@bot.message_handler(commands=['help', 'about'])
def help_message(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, 'Yo, you have done help')
    elif message.text == '/about':
        bot.send_message(message.chat.id, 'Bot shows zodiac signs compatibility')


@bot.message_handler(commands=['start', 'stop'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        item1 = types.KeyboardButton('Male')
        item2 = types.KeyboardButton('Female')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Choose your male', reply_markup=markup)
    if message.text == '/stop':
        markupr = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Bot is stopped', reply_markup=markupr)


regex = '|'.join(zodiac_signs)
first_sign = None
user_dict = []
male = None


@bot.message_handler(regexp=regex)
def signs(message):
    markup_remove = types.ReplyKeyboardRemove()
    global first_sign
    first_sign = message.text
    if len(user_dict) < 2:
        user_dict.append(first_sign)
    if len(user_dict) == 2:
        chance = choose_male(male, user_dict)
        bot.send_message(message.chat.id, str(chance), reply_markup=markup_remove)
        user_dict.clear()
        return
    print(user_dict)
    if message.text in zodiac_signs:
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
        bot.send_message(message.chat.id, 'Choose second sign ', reply_markup=markup)


@bot.message_handler(regexp='Male|Female')
def male(message):
    global male
    male = message.text
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


@bot.message_handler(content_types=['text'])
def another_message(message):
    bot.send_message(message.chat.id, 'YO press /start to begin')


bot.polling()
