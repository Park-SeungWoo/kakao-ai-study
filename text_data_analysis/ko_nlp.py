import numpy as np
import pandas as pd
from konlpy.tag import Okt
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

