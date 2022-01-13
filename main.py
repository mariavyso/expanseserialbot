from datetime import timedelta
import datetime
import requests
import re


#эта царь-функция проверяет сколько серий на сайте прямо сейчас
def check():
    z = requests.get(url)
    z.text
    regex = r"data:episode="
    test_str = z.text
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

#это царь-переменные, которые нужны во всех функциях
episodes = collection.find_one({}, {'episodes'})
new_episodes = matchNum
new_time = datetime.now()
old_time = new_time.strftime('%H:%M:%S')
delta  = timedelta(minutes=2)