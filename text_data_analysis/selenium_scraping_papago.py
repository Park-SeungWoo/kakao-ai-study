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


def papago_translate(dri, text, bef_text=''):
    translator = WebDriverWait(dri, 10).until(
        EC.visibility_of_element_located((By.ID, 'txtSource')))  # wait til loading
    translator.clear()
    translator.send_keys(text)

    WebDriverWait(dri, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[5]/p[1]'))
    )  # wait until translated

    time.sleep(0.5)
    translated_elem = WebDriverWait(dri, 10).until(
        EC.visibility_of_element_located((By.ID, 'txtTarget')))  # wait til displayed


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
        elif bef_text.lower() == tr_txt.lower():  # wait til translated
            continue
        else:
            break

    return tr_txt


@driver_close
def translate_words(dri, word_list):
    bef_txt = ''
    tr_dict = {}
    for t in word_list:  # multiple words
        tr_txt = papago_translate(dri, t, bef_txt)
        bef_txt = tr_txt
        tr_dict[t] = tr_txt
        time.sleep(0.5)  # to avoid blocking from server

    print(tr_dict)
    return tr_dict


# set virtual window's locale
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'ko'})

driver = webdriver.Chrome(executable_path=r'./text_data_analysis/Chrome_driver/chromedriver', chrome_options=options)
driver.get('https://papago.naver.com/?sk=ko&tk=en')
df = pd.read_excel('./text_data_analysis/scraping_datas/articles/221207_0249.xlsx', engine='openpyxl')

articles = ' '.join(df['Article'].tolist())  # get articles only

tokenizer = Okt()  # to use konlpy's pos tagging
tokens = tokenizer.pos(articles, norm=True, stem=True)  # I need pos tag to filter by pos

# removing stopwords
stopword_list = stopwords('ko')
stopword_list.update(['하다', '되다', '있다', '이다', '돼다', '않다', '그렇다', '아니다', '이렇다', '어떻다'])
cleaned_words = []
for item in tokens:
    if item[1] not in ['Josa', 'Eomi', 'Punctuation', 'Foreign']:
        if (item[0] not in stopword_list) and (len(item[0]) != 1):  # extract stopwords and the word which length is 1
            cleaned_words.append(item[0])

counted_dict = dict(Counter(cleaned_words))  # count
counted_sorted = sorted(counted_dict.items(), key=lambda x: x[1], reverse=True)  # sort by counts
top_words_dict = dict(counted_sorted[:100])  # get only top 100 frequent words

# translate
translated_dict = {}
tr_keys_dict = translate_words(driver, top_words_dict.keys())
tr_keys = list(tr_keys_dict.values())

# preprocessing translated keys
for key in tr_keys:
    key = key.replace('.', '').split(',')[0]

for idx, item in enumerate(top_words_dict.items()):
    if tr_keys[idx] in translated_dict.keys():
        translated_dict[tr_keys[idx] + f'{item[0]}'] = item[1]
    translated_dict[tr_keys[idx]] = item[1]


print(translated_dict)
print(top_words_dict)

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
