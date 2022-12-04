import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime
import time
import re

url = 'https://search.naver.com/search.naver?where=news&query='
# query = quote('데이터분석')
query = '데이터분석'

# web = urlopen(url + query)
# print(web)

web = requests.get(url + query).content
# print(web)
dom = BeautifulSoup(web, 'html.parser')

### div.sc_page => a.btn_next - aria-disabled = true : last page
titles = [news.get_text() for news in dom.find('div', {'class': 'group_news'}).find_all('a', {'class': 'news_tit'})]
news_a_tags = []  # a tag that connect to naver news site
for news in dom.find('div', {'class': 'group_news'}).find_all('a', {'class': 'info'}):
    if news.attrs['href'].startswith('https://n.news.naver.com/'):
        news_a_tags.append(news)

contents = []
for a_tag in news_a_tags:
    try:
        n_url = a_tag.attrs['href']
        n_web = requests.get(n_url, verify=False, timeout=1).content
        n_dom = BeautifulSoup(n_web, 'html.parser')
        contents.append([p.get_text() for p in n_dom.find('div', {'id': 'contents'})])
        time.sleep(2)
    except requests.exceptions.ReadTimeout as e:  # maybe it's because of the limit of http request.
        print(f"{n_url} : time out")

print(contents)