import requests
from bs4 import BeautifulSoup
import json
import os

req = requests.get('https://www.10000recipe.com/recipe/list.html')

html = req.text

# header = req.headers

# status = req.status_code

# is_ok = req.ok

soup = BeautifulSoup(html,'html.parser')

my_titles = soup.select(
    '#contents_area_full > ul > ul > li > div.common_sp_caption > div.common_sp_caption_tit.line2'
)
my_hrefs = soup.select(
    '#contents_area_full > ul > ul > li:nth-child(3) > div.common_sp_thumb > a'
)

data = {}

for title in my_titles:
    for href in my_hrefs:
        # print(title.text)
        # print(title.get('href'))
        data[title.text]='/www.10000recipe.com'+href.get('href')

with open(os.path.join('./','result1.json'),'w+',encoding='utf-8') as json_file:
    json.dump(data,json_file, ensure_ascii=False)