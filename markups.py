from telebot import types
import config
markup_remove = types.ReplyKeyboardRemove()

markup_greetings = types.ReplyKeyboardMarkup(row_width=3)
town_button = types.KeyboardButton('/Города')
package_button = types.KeyboardButton('/Корзина')
history_button = types.KeyboardButton('/История')
comments_button = types.KeyboardButton('/Комментарии')
prepurchase_button = types.KeyboardButton('/Предзаказ')
sos_button = types.KeyboardButton('/Поддержка')
work_button = types.KeyboardButton('/Работа')
payment_button = types.KeyboardButton('/Способы')
rules_button = types.KeyboardButton('/Правила')
markup_greetings.add(town_button, package_button, history_button, comments_button,
                     prepurchase_button, sos_button, work_button, payment_button, rules_button)

markup_greetings_2 = types.InlineKeyboardMarkup(row_width=1)
big_rules_button = types.InlineKeyboardButton('Большие правила', callback_data=config.global_rules)
channel = types.InlineKeyboardButton('Ссылка на канал', url=config.chat_channel)
markup_greetings_2.add(big_rules_button, channel)

markup_towns = types.InlineKeyboardMarkup(row_width=2)
novogir = types.InlineKeyboardButton('Nogogireevo', callback_data=config.test)
perovo = types.InlineKeyboardButton('Perovo', callback_data=config.test)
markup_towns.add(novogir, perovo)