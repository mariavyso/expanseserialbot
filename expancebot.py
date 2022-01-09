from datetime import datetime
import requests
import json
from html.parser import HTMLParser
import telebot
import pickle
import time
import telegram.ext
from telegram.ext import Updater, Dispatcher, CallbackContext
import telegram
from datetime import datetime, timedelta

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
e = datetime.now()
dt_string = e.strftime('\n%H:%M:%S')
file = open("data.txt", "w")
file.write(str(b))
file = open("data.txt", "a")  # append mode
file.write(dt_string)
file.close()

with open("data.txt", "r") as file:
    oldnum = first_line = file.readline()
    t1 = last_line = file.readlines()[-1]

token = '5071473434:AAFcvbhbgadvtM34eH1LVVTWVLFxV-39DZ4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"yo ✌️ ")


@bot.message_handler(commands=['answer'])
def answer(message):
    if str(b) > oldnum:
        bot.send_message(message.chat.id,'Yes, there is a new episode for u!')
    else:
        bot.send_message(message.chat.id,'Oh,dear! You should wait')


def check():
    if str(b) > oldnum:
        bot.send_message(1176786225,'Go!')
    else:
        return

while True:
    u = bot.get_updates(offset=(bot.last_update_id+1))
    bot.process_new_updates(u)
    time.sleep(1)  #на случай гавна
    oldtime = timedelta(hours=e.hour, minutes=e.minute, seconds=e.second)
    t2 = datetime.now()
    newtime = timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second)
    delta = timedelta(minutes=2)
    if newtime - oldtime > delta:
        check()
    else:
        time.sleep(2)

    
    



    





