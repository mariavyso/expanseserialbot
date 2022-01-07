import time
import requests
import json
from html.parser import HTMLParser
import telebot
import schedule
import time
import re
from telegram.ext import Updater

token = '5071473434:AAFcvbhbgadvtM34eH1LVVTWVLFxV-39DZ4'
bot = telebot.TeleBot(token)

def check_soap():
    z = requests.get('https://soap4.me/soap/The_Expanse/6/')
    z.text
    regex = r"data:episode="
    test_str = z.text
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
    if matchNum > 4:
        bot.send_message(1176786225,'I check it and there is a new episode!')
    else:
        bot.send_message(1176786225,'Nothing new')


while True:
    check_soap()
    time.sleep(3600)
