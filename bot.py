import markups
import config
import telebot
bot = telebot.TeleBot(config.access_token)

@bot.message_handler(commands=['start', 'help', 'stop'])
def send_welcome(message):
    print(message)
    greetings = 'Hello ' + message.from_user.first_name + ' Welcome to BOTNAME'
    if message.text == '/start':
        bot.send_message(message.from_user.id, greetings)
        bot.send_message(message.from_user.id, config.rules, reply_markup=markups.markup_greetings_2)
        bot.send_message(message.from_user.id, ' Выбери категорию', reply_markup=markups.markup_greetings)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Выбери категорию')
    elif message.text == '/stop':
        bot.send_message(message.from_user.id, 'Процесс остановлен', reply_markup=markups.markup_remove)


@bot.message_handler(commands=['Города', 'Корзина', 'История', 'Комментарии', 'Предзаказ',
                               'Поддержка', 'Работа', 'Способы', 'Правила'])
def goroda(message):
    if message.text == markups.town_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.package_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.history_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.comments_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.prepurchase_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.sos_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.work_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.payment_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)
    elif message.text == markups.rules_button.text:
        bot.send_message(message.from_user.id, 'test', reply_markup=markups.markup_towns)


@bot.callback_query_handler(func=lambda call: True)
def greeting_buttons(call):
    if call.data == config.global_rules:
        bot.send_message(call.from_user.id, config.rules)
    elif call.data == config.chat_channel:
        bot.send_message(call.from_user.id, config.chat_channel)
    elif call.data == config.test:
        bot.send_message(call.from_user.id, config.test)


# print(message) здесь много полезной инфы, типа id
bot.polling(none_stop=True, interval=1)

