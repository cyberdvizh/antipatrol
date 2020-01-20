from telebot import types
start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #, remove_keyboard=True
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

vote_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
vote_markup_btn1 = types.KeyboardButton('Да!', request_location=True)
vote_markup_btn2 = types.KeyboardButton('Нет.')
vote_markup.add(vote_markup_btn1, vote_markup_btn2)