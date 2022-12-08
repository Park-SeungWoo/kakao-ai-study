import numpy as np
import pandas as pd
from konlpy.tag import Okt
from stopwordsiso import stopwords
# from collections import Counter
from matplotlib import pyplot as plt
import nltk

# save variables as a file
import pickle

from text_data_analysis.naver_news_scraping import scrap_naver_news

## wordcloud
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

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
        if (len(word[0]) != 1) & (
                word[0] not in sw_list):  # one-length words are not necessary in this project, so I removed it.
            clean.append(word[0])

# print(clean)

plt.rc('font', family='Nanum GaRamYeonGgoc')  # font setting (Korean)
# plt.figure(figsize=(10, 5))

words_dict = nltk.Text(clean)
# words_dict.plot(15)
# print(words_dict)

word_freq = nltk.FreqDist(words_dict)
# print(word_freq.values())  # same as Counter

df = pd.DataFrame(list(word_freq.values()), word_freq.keys(), columns=['freq'])
# print(df)
df.sort_values(by='freq', ascending=False, inplace=True)
# print(df)

# df[:50].plot(kind='bar', legend=False, figsize=(15, 5))
# plt.show()

############################# same as above
# word_dict = dict(Counter(clean))
# word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
# # print(word_dict)
#
# # vlisualize
# plt.bar(list(zip(*word_dict))[0][:20], list(zip(*word_dict))[1][:20])  # same as [x[0] for x in word_dict][:20], [x[1] for x in word_dict][:20]
# plt.xticks(rotation=90)
# plt.show()
############################

# wordcloud

# print(dict(word_freq))

# word_cloud = WordCloud(font_path='/Users/seungwoosmac/Library/Fonts/BMJUA_ttf.ttf',
#                        width=1000,
#                        height=500,
#                        background_color='white',
#                        max_words=100,
#                        prefer_horizontal=True).generate_from_frequencies(word_freq)

# plt.figure(figsize=(10, 10))
# plt.imshow(word_cloud)
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()


#### using mask
# mask = np.array(Image.open('./text_data_analysis/assets/masks/korea_mask.jpg'))
# print(mask.shape)
# word_cloud = WordCloud(font_path='/Users/seungwoosmac/Library/Fonts/BMJUA_ttf.ttf',
#                        mask=mask,
#                        width=2000,
#                        height=1000,
#                        background_color='white',
#                        max_words=200,
#                        prefer_horizontal=True).generate_from_frequencies(word_freq)
#
# plt.figure(figsize=(10, 10))
# plt.imshow(word_cloud)
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()


####### add color
mask = np.array(Image.open('./text_data_analysis/assets/masks/youtube_mask.jpg'))
coloring = ImageColorGenerator(mask)
word_cloud = WordCloud(font_path='/Users/seungwoosmac/Library/Fonts/BMJUA_ttf.ttf',
                       mask=mask,
                       width=2000,
                       height=1000,
                       background_color='white',
                       max_words=200,
                       # prefer_horizontal=True
                       ).generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 10))
# plt.imshow(word_cloud.recolor(color_func=coloring), interpolation='bilinear')  # use image's own color
plt.imshow(word_cloud.recolor(colormap='Blues'), interpolation='bilinear')  # use matplotlib colormap
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('./text_data_analysis/wordclouds/word_cloud_youtube.png')
# plt.show()

# word_cloud.to_file('./text_data_analysis/wordclouds/word_cloud_youtube.png')
