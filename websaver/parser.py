import requests
from bs4 import BeautifulSoup
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
from parsed_data.models import Data
# import json
# import os

# req = requests.get('https://www.10000recipe.com/recipe/list.html')

# html = req.text

# # header = req.headers

# # status = req.status_code

# # is_ok = req.ok

# soup = BeautifulSoup(html,'html.parser')

# my_titles = soup.select(
#     '#contents_area_full > ul > ul > li > div.common_sp_caption > div.common_sp_caption_tit.line2'
# )
# my_hrefs = soup.select(
#     '#contents_area_full > ul > ul > li:nth-child(3) > div.common_sp_thumb > a'
# )

# data = {}

# for title in my_titles:
#     for href in my_hrefs:
#         # print(title.text)
#         # print(title.get('href'))
#         data[title.text]='/www.10000recipe.com'+href.get('href')

# with open(os.path.join('./','result1.json'),'w+',encoding='utf-8') as json_file:
#     json.dump(data,json_file, ensure_ascii=False)

def parse_Data():
    data = {}
    for a in range(1,10):
        #req = requests.get('https://www.10000recipe.com/recipe/list.html?order=reco&page=%d' %a)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        my_titles = soup.select(
            # '#contents_area_full > ul > ul > li > div.common_sp_caption > div.common_sp_caption_tit.line2'
        )
        my_hrefs = soup.select(
            # '#contents_area_full > ul > ul > li > div.common_sp_thumb > a'
        )
        my_materials = soup.select(
            # '#divConfirmedMaterialArea > ul > a > li'
)
        for title in my_titles:
            for href in my_hrefs:
                for mt in my_materials:
                    # print(title.text)
                    # print(title.get('href'))
                    data[title.text]='/www.10000recipe.com'+href.get('href')
    return data

if __name__=='__main__':
    blog_data_dict = parse_Data()
    for t, l in blog_data_dict.items():
        Data(title=t, link=l).save()
