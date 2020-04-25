import glob
import json
from pprint import pprint

files = glob.glob('json/*.json')
followers={}
for f in files:
    with open(f) as f:
        data = json.load(f)
        for node in data['data']['user']['edge_followed_by']['edges']:
            followers[node['node']['id']] = {
                'id': node['node']['id'],
                'username': node['node']['username'],
                'name': node['node']['full_name'],
                'is_followed': node['node']['followed_by_viewer'],
            }
followers = list(followers.values())

with open('followers.json','w', encoding='utf8') as f:
    json.dump(followers, f)
print('Дел сделано')
        