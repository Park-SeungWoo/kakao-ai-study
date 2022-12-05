import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime
import time
import re

pd.set_option('expand_frame_repr', False)  # show every columns, rows

url = 'https://search.naver.com/search.naver?where=news&query="{}"&start={}'
# query = quote('데이터분석')
query = '데이터분석'

# web = urlopen(url + query)
# print(web)

# titles = [news.get_text() for news in dom.find('div', {'class': 'group_news'}).find_all('a', {'class': 'news_tit'})]
news_a_tags = []  # a tag that connect to NAVER news site
max_page = 5  # page limit
for page in range(1, max_page * 10 + 1, 10):  # paging query : start=1, 11, 21, ...
    web = requests.get(url.format(query, page)).content
    dom = BeautifulSoup(web, 'html.parser')
    is_last_page = dom.find('div', {'class': 'sc_page'}).find('a', {'class': 'btn_next'}).attrs['aria-disabled']  # if last page : true, str type
    is_last_page = False if is_last_page == 'false' else True  # convert to bool type
    if not is_last_page:
        for news in dom.find('div', {'class': 'group_news'}).find_all('a', {'class': 'info'}):
            # print(news.attrs['href'])
            if news.attrs['href'].startswith('https://n.news.naver.com/'):
                news_a_tags.append(news)
    else:
        break




def date_string_to_timestamp(d: str):
    d = d.replace(" ", '')
    ymd = d[:11]
    t = d[13:]
    am_pm = d[11:13]
    am_pm = 'am' if am_pm == '오전' else 'pm'
    return pd.Timestamp(ymd + t + am_pm)


def contents_preprocessing(a: str):
    a = a.replace('\n', '')
    a = a.replace('동영상 뉴스', '')
    a = a.strip()
    pattern = re.compile(r'\'')
    a = pattern.sub('', a)
    return a


header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
titles = []
contents = []
dates = []
agencies = []
urls = []
for a_tag in news_a_tags:
    try:
        n_url = a_tag.attrs['href']  # url
        # n_web = requests.get(n_url, verify=False, timeout=1).content
        # n_web = requests.get(n_url).content
        n_web = requests.get(n_url, headers=header, timeout=2).content
        n_dom = BeautifulSoup(n_web, 'html.parser')
        content = n_dom.find('div', {'id': 'dic_area'}).get_text()  # contents
        title = n_dom.find('h2', {'id': 'title_area'}).get_text()  # title
        date = n_dom.find('span', {'class', 'media_end_head_info_datestamp_time'}).get_text()  # date
        agency = n_dom.find('em', {'class': 'media_end_linked_more_point'}).get_text()  # news agency
        content = contents_preprocessing(content)  # preprocessing
        date = date_string_to_timestamp(date)  # convert to pd.Timestamp
        titles.append(title)
        contents.append(content)
        dates.append(date)
        agencies.append(agency)
        urls.append(n_url)
        print(f'{title} processing complete')
        time.sleep(0.3)
    except requests.exceptions.ReadTimeout as e:  # maybe it's because of the limit of http request.
        print(f"{n_url} : time out")
    except:
        print('something went wrong check it out')

article_df = pd.DataFrame({
    'Title': titles,
    'Article': contents,
    'Agency': agencies,
    'Date': dates,
    'URL': urls
})

# print(article_df)
article_df.to_excel(f'./text_data_analysis/scraping_datas/articles/{datetime.now().strftime("%y%m%d_%H%M")}.xlsx',
                    index=False, encoding='utf-8')  # save as an excel file
