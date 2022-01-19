from typing import Text
import pymongo
import certifi
import time
import telebot
from telegram import message
import validators
from datetime import datetime, timedelta, date
import datetime
import requests
import re


token = '5071473434:AAFZPmdZpIDWnIguEzdYsqIdzlC8Py3sIZU'
bot = telebot.TeleBot(token)
client = pymongo.MongoClient(
    "mongodb+srv://mashavyso:Fdert457nDSWEM@cluster0.qyggr.mongodb.net/bot?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)
db = client.bot
collection = db.coll


#это бот здоровается
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"yo, man ✌️ ")
    

#эта ф-я заводит новый док с сериалом
def add_serial(url):
    dict1 = {'serial' : url, 'episodes': '', 'data': '', 'time' : ''}
    collection.insert_one(dict1)
    


#эта царь-функция проверяет сколько серий на сайте прямо сейчас
url = 'https://soap4.me/soap/24_hours/1/'
# def check(matchNum, group):
z = requests.get(url)
z.text
regex = r"data:episode=\"(\d)\"[\S\s]*?показ:</span> ([-0-9]+)<br />"
test_str = z.text
matches = re.finditer(regex, test_str)
for matchNum, match in enumerate(matches, start=1):
    groupNum = 2
    group = match.group(groupNum)
        # print ('Episode: {matchNum} was on air {group}'.format(matchNum = matchNum, group = match.group(groupNum)))
    
    
data = group
new_data = date.today()
deltadata = timedelta(days = 2)
new_episodes = matchNum
new_time = datetime.datetime.now()
#print (new_time)
old_time = new_time.strftime('%H:%M:%S')
#print (old_time)
delta  = timedelta(minutes=2)

#эта ф-я производит апдейт данных дока с определенным сериалом эпизодами и временем
def updatedb(url):
    a =collection.find_one({'serial' : url})
    collection.update_many(a,{'$set': {'episodes': matchNum, 'data': data,'time': old_time}}, upsert=False)



#это функция делает проверку по команде от юзера
@bot.message_handler(commands=['answer']) 
def answer(message):
    a = list(collection.find({},{'serial':1, 'data':1, '_id':0}))
    print (a)
    f = 'Last updates: \n'
    index = 1
    for d in a:
        f = f + str(index) + ' ' + d['serial'] + ' ' + d['data'] + ('\n')
        index +=1
        print (f)
    bot.send_message(message.chat.id, f)


#показываем список сериалов, за которыми следит бот
@bot.message_handler(commands=['mylist'])
def show_serials(message):
    #эта ф-я выводит все линки сериалов в коллекции
    a = list(collection.find({}))
    x = "Your serials: \n"
    index = 1
    for line in a:
        x = x + str(index)+ ' ' + line['serial'] + ',' + ('\n') 
        index +=1
    bot.send_message(message.chat.id, x)
    

def list_serials():
    #эта ф-я выводит все линки сериалов в коллекции
    return list(collection.find({}))

    

context = None

#удаляем ненужный сериал
@bot.message_handler(commands=['delete'])
def delete(message):
    global context
    context = "delete"
    bot.send_message(message.chat.id, "Here is your serial's list, send me the number, which I should delete", show_serials(message))


#эта ф-я забирает от юзера новый сериал для наблюдения
@bot.message_handler(commands=['add'])
def add(message):
    global context
    context = "add"
    bot.send_message(message.chat.id, "Give me the link")      


def get_url_from_list(number):
    #print("get_url_from_list", number)
    number = int(number) - 1
    #print("number", number)
    all_serials = list_serials()
    #print("all_serials", all_serials)
    serial = all_serials[number]
    #print("serial", serial)
    url = serial['serial']
    return url



@bot.message_handler(content_types=['text'])   
def text(message):
    global context
    #print()
    # print(f">>> text. {context}")
    # print(message)
    # print()
    if context == "delete":
        #print("in delete")
        number = message.text
        #print(number)
        url = get_url_from_list(number)
        #print(url)
        # #эта ф-я удаляет документ с сериалом
        collection.delete_one({'serial': url})
        bot.reply_to(message, 'Okay, I will delete it')
        context = None
        #print("DONE")
    elif context == "add":
        url = message.text
        if validators.url(message.text) == True:
            add_serial(url)
            a =collection.find_one({'serial' : url})
            collection.update_many(a,{'$set': {'episodes': matchNum, 'data': data, 'time': old_time}}, upsert=False)
            bot.reply_to(message, "Done")
            context = None
        else:
            pass
    else:
        pass
    
        # process text input



    

#это функция автоматической проверки новой серии каждые 2 минуты
def time_check():
    a = updatedb(url)    #это функция из pdr.py
    if new_time - old_time > delta:
        if new_data - data > deltadata:
            bot.send_message(1176786225,'Go watch!')
            a
        else:
            return
    else:
        return



#запускаем бота
while True:
    u = bot.get_updates(offset=(bot.last_update_id+1))
    bot.process_new_updates(u)
    time.sleep(1)