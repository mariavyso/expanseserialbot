import pymongo
import certifi



client = pymongo.MongoClient(
    "mongodb+srv://mashavyso:Fdert457nDSWEM@cluster0.qyggr.mongodb.net/bot?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)
db = client.bot
collection = db.coll


#эта ф-я заводит новый док с сериалом
def add_serial(url):
    dict1 = {'serial' : url, 'episodes': '', 'time' : ''}
    collection.insert_one(dict1)

#эта ф-я производит апдейт данных дока с определенным сериалом эпизодами и временем
def updatedb(url):
    a =collection.find_one({'serial' : url})
    collection.update_many(a,{'$set': {'episodes': matchNum, 'time': old_time}}, upsert=False)

#эта ф-я удаляет документ с сериалом
def delete_serial(url):
    collection.find_one({'serial' : url})
    collection.delete_one({'serial': url})

#эта ф-я выводит все линки сериалов в коллекции
def find_serials():
    a = list(collection.find({}))
    for line in a:
        print(line['serial'])

