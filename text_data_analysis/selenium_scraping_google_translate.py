from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from collections import Counter
from konlpy.tag import Okt
from stopwordsiso import stopwords
import pandas as pd

from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

from bs4 import BeautifulSoup
import time

import warnings

warnings.filterwarnings('ignore')


# methods
def get_Chrome_driver(url):
    driver = webdriver.Chrome(
        executable_path=r'./text_data_analysis/Chrome_driver/chromedriver')  # have to download chromedriver file and set path
    # driver.maximize_window()
    driver.get(url)
    return driver


def google_translate(text, driver, bef_text=''):
    # translate and get translated text
    translator = driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
    translator.clear()  # clear before translation.
    translator.send_keys(text)  # send_keys(), clear(), click()

    # There is an error when I get translated text promptly after executing 'send_keys()' method.
    # It's because there is some delays to translate and display in the web browser.
    # So I handled it by waiting til displayed, and get translated text.
    while True:
        try:
            is_translated = driver.find_element_by_xpath(
                '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]')
            translated = is_translated.text  # when the text displayed in web browser, these below codes will ve executed.
            if translated.endswith('\n...') and (not text.endswith('\n...')):  # wait before translated again
                continue
            if translated == bef_text:  # wait before translated again
                continue
            print(f'translation "{text}" completed : "{translated}"')
            return translated
        except:
            continue

        ### Google displays each sentence wrapped with span tag.
        ### So if you want to get each sentence, use these code.
        ## If it doesn't displayed translated text, It will return empty list.
        # translated_elem = driver.find_elements_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span[*]/span')
        # if len(translated_elem) != 0:
        #     for elem in translated_elem:
        #         translated += elem.text  # If the text displayed in web browser, this code will be executed.
        # else:
        #     continue
        # return translated


# main process
if __name__ == '__main__':
    DF = pd.read_excel('./text_data_analysis/scraping_datas/articles/221207_0249.xlsx', engine='openpyxl')
    TR_URL = 'https://translate.google.co.kr/?sl=ko&tl=en&op=translate'
    stopwords_list = list(stopwords('ko'))
    stopwords_list.extend(['하다', '되다', '있다', '이다', '돼다', '않다', '그렇다', '아니다', '이렇다', '어떻다'])
    tokenizer = Okt()
    articles = ' '.join(DF['Article'].tolist())

    pos_tagged = tokenizer.pos(articles, norm=True, stem=True)

    # extract useful words only
    cleaned = []
    for word in pos_tagged:
        if word[1] not in ['Josa', 'Eomi', 'Punctuation', 'Foreign']:
            if (len(word[0]) != 1) & (word[0] not in stopwords_list):
                cleaned.append(word[0])

    counted = dict(Counter(cleaned))
    counted = dict(sorted(counted.items(), key=lambda x: x[1], reverse=True)[:100])

    translated_dict = {}
    bef_text = ''
    driver = get_Chrome_driver(TR_URL)
    for item in counted.items():
        translated = google_translate(item[0], driver, bef_text)
        translated_dict[translated] = item[1]
        bef_text = translated
        time.sleep(0.5)  # avoid blocking

    # print(counted, translated_dict, sep='\n')
    masking = np.array(Image.open('./text_data_analysis/assets/masks/python_mask.jpg'))
    coloring = ImageColorGenerator(masking)

    word_cloud = WordCloud(font_path='/Users/seungwoosmac/Library/Fonts/BMJUA_ttf.ttf',
                           width=1000,
                           height=500,
                           background_color='white',
                           max_words=100,
                           mask=masking
                           # prefer_horizontal=True
                           ).generate_from_frequencies(translated_dict)

    plt.figure(figsize=(10, 10))
    plt.imshow(word_cloud.recolor(color_func=coloring), interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

    # finish
    driver.close()
    driver.quit()