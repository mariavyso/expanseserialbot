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



def callback_minute(context: telegram.ext.CallbackContext):
    if matchNum < a:
        context.bot.send_message(1176786225,'Go watch!')
    else:
        context.bot.send_message(1176786225,'fuck!')
job_minute = j.run_repeating(callback_minute, interval=60)