import requests
import json
from html.parser import HTMLParser
import telebot

token = '5071473434:AAHwt3NGiWwiB_Z_5lEbYGDOa7gSoS7AYfo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")

###@bot.message_handler(commands=['answer'])
###def start_message(message):
  
  
#   z = requests.get('https://soap4.me/soap/The_Expanse/6/')
#   z.text
#   import re
#   regex = r"data:episode="
#   test_str = z.text
#   matches = re.finditer(regex, test_str, re.MULTILINE)
#   for matchNum, match in enumerate(matches, start=1):
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
#   for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
        
#     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# if matchNum > 3:
#     print ('yes')
# else:
#     print ('no')
 
bot.infinity_polling()
