from bs4 import BeautifulSoup
import requests

username = 'coccume'
url = f'https://www.instagram.com/{username}/'

def get_html(url):
    response=requests.get(url)
    return response.text


soup = BeautifulSoup(get_html(url))
got = soup.findAll('script', src='')
ind = got[4].text.find('"id"')
ans = got[4].text[ind+6:ind+16:]
print(ans)