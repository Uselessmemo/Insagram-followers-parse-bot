import requests
import json
import time

username = ''#
iser_id = #
headers = {
    #
}


index=1
after=None
done_users=0
while True:
    after_val = f',"after":"{after}"' if after else ''  
    params = (
        ('query_hash', ''),#
        ('variables', f'{{"id":"{iser_id}","include_reel":true,"fetch_mutual":true,"first":50{after_val}}}'),
    )
    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

    if(response.status_code == 200):
        response=response.json()
        with open(f'json/followers_{index}.json', 'w',) as f:
            json.dump(response, f)
        f.close()
    else:
        print('Fail',response.status_code)
        exit()
    
    after = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers = response['data']['user']['edge_followed_by']['count']
    in_current_batch = len(response['data']['user']['edge_followed_by']['edges'])
    done_users+=in_current_batch
    print(f'Обработано {done_users}/{all_followers}')

    if not response['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        print('Обработка закончена')
        exit()
        
    index+=1
    time.sleep(5 if index % 10 != 0 else 10)
    
# fill where comented