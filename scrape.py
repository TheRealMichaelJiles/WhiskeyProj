import requests
from bs4 import BeautifulSoup 
import pymongo
from pymongo import MongoClient
import untangle

connString = MongoClient('mongodb+srv://themichaeljiles:ndLG6iVXWZyDgl08@origin.jfgechg.mongodb.net/?retryWrites=true&w=majority')

db = connString['Origin']
collection = db['WhiskeyBase']

proxies = {
'http': '209.38.224.68:8080',
}

headers = {
    'authority': 'www.totalwine.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': 'https://www.totalwine.com/search/all?text=aberlour%2012&pageSize=24&aty=1,1,0,1',
    'accept-language': 'en-US,en;q=0.9',
    'scheme': 'https'
}
r = requests.get('https://www.totalwine.com/Product-en-USD-0.xml', headers = headers)

content = r.content.decode()
obj = untangle.parse(content)
location = obj.urlset.url[0].loc
collection.insert_one({'location':location.cdata})

# print(obj.url[0])

# soup = BeautifulSoup(r.content.decode(), "html.parser")
# art = soup.find('article')
# print(art)