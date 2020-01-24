# -*- config: utf-8
'''import telebot
import markups as m
bot = telebot.TeleBot("995630658:AAF6W6Ksg6fOhd3Zi20McY2OHOekFpAKk9Y")

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, "Хотите помочь?", reply_markup=m.vote_markup)
        bot.register_next_step_handler(msg, afterstart) #askSource
        isRunning = True

def afterstart(message):
    chat_id = message.chat.id
    text = message.text
    channel_id = 1001360951458
    if text == ("Нет."):
        global isRunning
        isRunning = False
        bot.send_message(chat_id, 'Если решитесь, нажмите /start', reply_markup=m.start_markup)
        bot.register_next_step_handler(message, start_handler)
    else:
        bot.forward_message(channel_id, chat_id, text)
        bot.send_message(message.chat.id, 'Принимаю местоположение')
        bot.register_next_step_handler(message, afterstart) #askSource
        bot.send_message(chat_id, "Хотите помочь еще?", reply_markup=m.vote_markup)
       # bot.register_next_step_handler(msg, start_handler) как вернуться ?


isRunning = False

bot.polling(none_stop=True)'''

import telebot

bot = telebot.TeleBot("995630658:AAF6W6Ksg6fOhd3Zi20McY2OHOekFpAKk9Y")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['record'])
def record(message):
    print('Чтобы прервать запись, набери q')
    while True:
        print('Потратил: ')
        trata = message
        if trata == 'q':
            break
        else:
            records.append(int(trata))

def summa():
    zatratq = 0
    for chisla in records:
        zatratq = zatratq + chisla
    print('Сегодня ты потратил ' + str(zatratq) + ' рублей.')

records = []
for chisla in records:
    print(chisla)
summa()

bot.polling()

