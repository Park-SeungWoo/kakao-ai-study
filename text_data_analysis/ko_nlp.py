import numpy as np
import pandas as pd
from konlpy.tag import Okt
from stopwordsiso import stopwords
from collections import Counter
from matplotlib import pyplot as plt
import nltk
import os
import pickle
from text_data_analysis.advanced_scraping import scrap_naver_news


#### test
# scrap_naver_news('데이터분석')

# tokenizer = Okt()
# tokens = tokenizer.pos('아버지가 방에 들어가신다.', norm=True, stem=True)
# print(tokens)

# sen = 'NLTK is a natural language processing library'
# print(nltk.word_tokenize(sen))

df = pd.read_excel('./text_data_analysis/scraping_datas/articles/221207_0249.xlsx', engine='openpyxl')
# print(df)

articles = df['Article'].tolist()
# print(articles)
articles = ' '.join(articles)

tokenizer = Okt()
tokens = tokenizer.pos(articles, norm=True, stem=True)  # tokenize & pos tagging
# print(tokens)

sw_list = list(stopwords('ko'))
sw_list.extend(['하다', '있다', '되다', '이다', '돼다', '않다', '그렇다', '아니다', '이렇다', '그렇다', '어떻다'])
clean = []
for word in tokens:  # tuple
    if word[1] not in ['Josa', 'Eomi', 'Punctuation', 'Foreign']:  # filter by POS
        if (len(word[0]) != 1) & (word[0] not in sw_list):  # one-length words are not necessary in this project, so I removed it.
            clean.append(word[0])

# print(clean)

word_dict = dict(Counter(clean))
word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
# print(word_dict)

# vlisualize
plt.rc('font', family='Nanum GaRamYeonGgoc')  # font setting (Korean)
plt.figure(figsize=(10, 5))
plt.bar(list(zip(*word_dict))[0][:20], list(zip(*word_dict))[1][:20])  # same as [x[0] for x in word_dict][:20], [x[1] for x in word_dict][:20]
plt.xticks(rotation=90)
plt.show()

# TF-IDF
