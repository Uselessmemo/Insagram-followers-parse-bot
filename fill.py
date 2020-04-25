import json
import requests
import time
import csv
from pprint import pprint


with open('followers.json',encoding='utf8') as f:
    followers = json.load(f)

index = 0
followers_filled = []
for user in followers:
    username = user['username']
    headers = {
        #
    }

    params = (
        ('__a', '1'),
    )  
    response = requests.get(f'https://www.instagram.com/{username}/', headers=headers, params=params).json()
    user['followed_by'] = response['graphql']['user']['edge_followed_by']['count']
    user['followes'] = response['graphql']['user']['edge_follow']['count']
    user['publications'] = response['graphql']['user']['edge_owner_to_timeline_media']['count']
    user['bio'] = response['graphql']['user']['biography']
    followers_filled.append(user)
    print(f'Итерация {index}/{len(followers)}')
    time.sleep(1 if index % 10 != 0 else 3)
    index += 1

with open('result.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('№', 'Тег', 'ID', 'Имя', 'Биография', 'Фоловеров', 'Подписок', 'Публикаций', 'Подписан ли я'))
    cnt = 1
    for user in followers_filled:
        writer.writerow((cnt, user['username'], user['id'],user['name'], user['bio'], user['followed_by'], user['followes'], user['publications'], user['is_followed']))
        cnt += 1

# fill where comented