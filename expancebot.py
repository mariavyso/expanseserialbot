import requests
import json
from html.parser import HTMLParser
import telebot
import pickle
import time
import telegram.ext
from telegram.ext import Updater, Dispatcher, CallbackContext

z = requests.get('https://soap4.me/soap/The_Expanse/6/')
z.text
import re
regex = r"data:episode="
test_str = z.text
matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

b = matchNum
pickle.dump(b, open('data.txt', 'wb'))
a = pickle.load(open('data.txt', 'rb'))

token = '5071473434:AAFcvbhbgadvtM34eH1LVVTWVLFxV-39DZ4'
bot = telebot.TeleBot(token)
u = Updater('5071473434:AAFcvbhbgadvtM34eH1LVVTWVLFxV-39DZ4', use_context=True)
j = u.job_queue


#@bot.message_handler(commands=['start'])
#def start(message):
    #bot.send_message(message.chat.id,"yo ✌️ ")
#job_minute = j.run_repeating(start, interval=60, first=10)

#@bot.message_handler(commands=['answer'])
#def answer(message):
   # if matchNum > a:
       # bot.send_message(message.chat.id,'Yes, there is a new episode for u!')
    #else:
        #bot.send_message(message.chat.id,'Oh,dear! You should wait')
#job_minute = j.run_repeating(answer, interval=60, first=10)

from telegram.ext import CommandHandler
def callback_alarm(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='BEEP')

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a timer for 1 minute!')

    context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)

timer_handler = CommandHandler('timer', callback_timer)
u.dispatcher.add_handler(timer_handler)

def callback_minute(context: telegram.ext.CallbackContext):
    if matchNum < a:
        context.bot.send_message(1176786225,'Go watch!')
    else:
        return
job_minute = j.run_repeating(callback_minute, interval=60)