import logging
import sys
from typing import Text
import pymongo
import certifi
import time
import telebot
import validators
from datetime import datetime, timedelta, date
import datetime
import requests
import re

#global variables
TOKEN = '5071473434:AAFZPmdZpIDWnIguEzdYsqIdzlC8Py3sIZU'
bot = telebot.TeleBot(TOKEN)
CLIENT = pymongo.MongoClient(
    #it is demo project, so this password leads to not-production database, I understand that it is not secure, but here it is to simplify deploy
    "mongodb+srv://mashavyso:Fdert457nDSWEM@cluster0.qyggr.mongodb.net/bot?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)
DB = CLIENT.bot
collection = DB.coll

CONTEXT_OF_MESSAGE = None


#function to check episodes and date of release
def reg_check(url):
    parse_url = requests.get(url)
    test_str = parse_url.text
    regex = r"data:episode=\"(\d+)\"[\S\s]*?показ:</span> ([-0-9]+)<br />"
    matches = re.finditer(regex, test_str)
    for matchNum, match in enumerate(matches, start=1):
        groupNum = 2
        group = match.group(groupNum)
    return group, matchNum

        

  
#start bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"yo, man ✌️ ")
    #log.info("hello")

#function to add new doc for serial in database
def add_serial_to_database(url):
    dict1 = {'serial' : url, 'episodes': '', 'data': '', 'time' : ''}
    collection.insert_one(dict1)
    #log.info("add serial to database")

#function to update doc with serial with episodes and date of release and time of checking
def update_database(url):
    date_of_release, episodes = reg_check(url) 
    time_of_check = datetime.datetime.now().strftime('%H:%M:%S')
    a =collection.find_one({'serial' : url})
    collection.update_many(a,{'$set': {'episodes': episodes, 'data': date_of_release,'time': time_of_check}}, upsert=False)
    #log.info("update db")



#function to check updates by user command via bot
@bot.message_handler(commands=['answer']) 
def answer(message):
    list_of_serials = list(collection.find({},{'serial':1, 'data':1, '_id':0}))
    last_updates = 'Last updates: \n'
    index = 1
    for serial in list_of_serials:
        last_updates = last_updates + str(index) + ' ' + serial['serial'] + ' ' + serial['data'] + ('\n')
        index +=1
    bot.send_message(message.chat.id, last_updates)
    #log.info("answered you")


#function to show list of user's serials via bot
@bot.message_handler(commands=['mylist'])
def show_serials(message):
    your_list = "Your serials: \n"
    index = 1
    for serial in list_serials():
        your_list = your_list + str(index)+ ' ' + serial['serial'] + ',' + ('\n') 
        index +=1
    bot.send_message(message.chat.id, your_list)
    #log.info("showed list")
  
#fuction fo call list of serials from database
def list_serials():
    return list(collection.find({}))  
  

#function to delete serial from user's list via bot
@bot.message_handler(commands=['delete'])
def delete(message):
    global context
    context = "delete"
    bot.send_message(message.chat.id, "Here is your serial's list, send me the number, which I should delete", show_serials(message))


#function to add new serial to your list via bot
@bot.message_handler(commands=['add'])
def add(message):
    global context
    context = "add"
    bot.send_message(message.chat.id, "Give me the link")      

#function to get url of serial from database
def get_url_from_list(number):
    number = int(number) - 1
    all_serials = list_serials()
    serial = all_serials[number]
    url = serial['serial']
    return url

#function to save user input in right places via context
@bot.message_handler(content_types=['text'])   
def text(message):
    global context
    if context == "delete":
        number = message.text
        url = get_url_from_list(number)
        collection.delete_one({'serial': url})
        bot.reply_to(message, 'Done, I deleted it')
        context = None
    elif context == "add":
        url = message.text
        if validators.url(message.text) == True:
            add_serial_to_database(url)
            reg_check(url)
            update_database(url)
            bot.reply_to(message, "Done, I added it")
            context = None
        else:
            bot.reply_to(message, "Send me correct URL!")
    else:
        pass
    
    

#function to autocheck new episodes and inform user about it
def autocheck(url, date_of_release, episodes):
    new_data = datetime.datetime.now()
    deltadata = timedelta(days = 2)
    matchNum = reg_check(url)
    new_episodes = matchNum[-1]
    if new_data - date_of_release > deltadata:
        if new_episodes>episodes:
            bot.send_message(1176786225,('Go watch this one: {}!'.format (url)))
            update_database(url)
        else:
            return
    else:
        return
    #log.info("did autocheck")

   

def all_serials_check():
    for serial in list_serials():
        data = serial['data']
        date_of_release = datetime.datetime.strptime(data, '%Y-%m-%d')
        episodes = serial['episodes']
        url = serial['serial']
        autocheck(url, date_of_release, episodes)
        #log.info("did serial check")

log = logging.getLogger(__name__)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)       

def main():
    #запускаем бота
    last_check_at = datetime.datetime(2000, 1, 1)
    while True:
        u = bot.get_updates(offset=(bot.last_update_id+1))
        bot.process_new_updates(u)
        time.sleep(1)
        new_time = datetime.datetime.now()
        delta  = timedelta(minutes=2)
        if new_time - last_check_at > delta:
            all_serials_check()
            log.debug(f"Time is not in data_grid")
            log.info("go check def all serials")
        else:
            time.sleep(4)
            
        last_check_at = datetime.datetime.now()


       



if __name__ == "__main__":
    main()

