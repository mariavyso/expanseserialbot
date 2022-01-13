import time
import telebot
import validators
import pdr



token = '5071473434:AAFZPmdZpIDWnIguEzdYsqIdzlC8Py3sIZU'
bot = telebot.TeleBot(token)


#это бот здоровается
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"yo, man ✌️ ")

#эта ф-я забирает от юзера новый сериал для наблюдения
@bot.message_handler(content_types=['text'])
def add(message):
    a = pdr.add_serial(url)           #это функция из pdr.py
    url = validators.url(message.text)    #это мы валидируем сообщение юзера -- юрл или нет.
    if url == True:
        bot.reply_to(message, "I'll save it for you") and a
    else:
        bot.reply_to(message, "Try again and send me real link to your serial!")


#это функция делает проверку по команде от юзера
@bot.message_handler(commands=['answer'])
def answer(message):
    if new_episodes > episodes:
        bot.send_message(message.chat.id,'Yes, there is a new episode for u!')
    else:
        bot.send_message(message.chat.id,'You should wait')


#это функция автоматической проверки новой серии каждые 2 минуты
def time_check():
    a = pdr.updatedb(url)    #это функция из pdr.py
    if new_time - old_time > delta:
        if new_episodes > episodes:
            bot.send_message(1176786225,'Go!')
            a
        else:
            return
    else:
        return


#показываем список сериалов, за которыми следит бот
@bot.message_handler(commands=['mylist'])
def show_serials(message):
    a = pdr.find_serials()            #это функция из pdr.py
    bot.send_message(message.chat.id, a)


#удаляем ненужный сериал
@bot.message_handler(commands=['delete'])
def delete(message):
    url = validators.url(message.text)
    a = pdr.delete_serial(url)               #это функция из pdr.py
    if url == True:
        bot.reply_to(message, "I'll delete it for you")
        a
    else:
        bot.reply_to(message, "Send me a link")



#запускаем бота
while True:
    u = bot.get_updates(offset=(bot.last_update_id+1))
    bot.process_new_updates(u)
    time.sleep(1)