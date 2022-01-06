import requests
import json
from html.parser import HTMLParser
import telebot

z = requests.get('https://soap4.me/soap/The_Expanse/6/')
z.text
import re
regex = r"data:episode="
test_str = z.text
matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

token = '5071473434:AAHwt3NGiWwiB_Z_5lEbYGDOa7gSoS7AYfo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(commands=['answer'])
def start_message(message):
    if matchNum > 3:
        print ('Yes, there is a new episode for u!')
        else:
            print ('Oh,dear! You should wait')
 
bot.infinity_polling()
