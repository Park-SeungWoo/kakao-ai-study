from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from collections import Counter
from konlpy.tag import Okt
from stopwordsiso import stopwords
import pandas as pd
import numpy as np

from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image

import time
import warnings

warnings.filterwarnings('ignore')


def driver_close(func):
    def wrapper(*args, **kwargs):
        dri = args[0]
        res = func(*args, **kwargs)
        dri.close()
        dri.quit()
        return res
    return wrapper


def NLP_count(PATH):
    pass


def papago_translate(dri, text, bef_text=''):
    translator = WebDriverWait(dri, 10).until(EC.visibility_of_element_located((By.ID, 'txtSource')))  # wait til loading
    translator.clear()
    translator.send_keys(text)
    translated_elem = WebDriverWait(dri, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[5]/div/span')))  # wait til displayed

    # PAPAGO displays text that has not yet been translated by pasting '...' after the word.
    # The changes in translated text over time are like this.
    # (word) => none -> tr_txt... -> tr_txt => (new word) => tr_txt -> tr_txt... -> new_tr_txt... -> new_tr_txt
    # And elem.text returns a text exactly in that time. I think elem saves specific element's information, and when we do '.text', it finds that element and get text.
    # The text can be changed while we checking the conditions.
    # So I made a variable to save text to prevent that the text changes while checking the conditions.
    while True:
        tr_txt = translated_elem.text
        if tr_txt.endswith('...'):  # wait til translated
            continue
        elif bef_text == tr_txt:  # wait til translated:
            continue
        else:
            break

    return tr_txt


@driver_close
def translate_words(dri, word_list):
    bef_txt = ''
    tr_li = []
    for t in word_list:
        tr_txt = papago_translate(dri, t, bef_txt)
        bef_txt = tr_txt
        tr_li.append(tr_txt)
        time.sleep(0.5)
    return tr_li


driver = webdriver.Chrome(executable_path=r'./text_data_analysis/Chrome_driver/chromedriver')
driver.get('https://papago.naver.com/?sk=ko&tk=en')
print(translate_words(driver, ['안녕', '그래', '언제', '싫어', '메롱']))
