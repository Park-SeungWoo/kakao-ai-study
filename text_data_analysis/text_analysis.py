import nltk  # doesn't have ko nlp
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import re

# sentence = 'NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength text_data_analysis libraries, and an active discussion forum.'
# token = nltk.word_tokenize(sentence)
# # print(token)
#
# pos = nltk.pos_tag(token)
# # print(pos)
#
# # N~ NOUN, V~ verb, j~, a~ adj
#
# Swords= stopwords.words('english')
# # print(len(Swords))
# # print(Swords)  # check built-in stopwords, modifiable, lower case
# # print(stopwords.fileids())
#
# # add . and , in stopwords list
# Swords.extend(['.', ','])
#
# res = [x for x in token if x.lower() not in Swords]  # take only not stopwords
# # print(len(res))
# # print(res)
# # l = [x for x in res if x.isalnum()]
# # print([x for x in res if x not in l])
#
# ######### lemmatizing (stemming in konlp)
# # nltk.download('omw-1.4')
# lem = nltk.wordnet.WordNetLemmatizer()
#
# # print(lem.lemmatize('cats'))
# # print(lem.lemmatize('better', pos='a'))
# # print(lem.lemmatize('ran', pos='v'))

################ real practice
# Swords = stopwords.words('english')
# Swords.extend([',', '.'])
# lem = nltk.wordnet.WordNetLemmatizer()
#
# f = open('./text_data_analysis/scraping_datas/moviereview.txt', 'r')
# txtdata = f.readlines()
#
# sentence = txtdata[1]
# token = nltk.word_tokenize(sentence)
# tagged_tokens = nltk.pos_tag(token)  # pos tagging
#
# lemmas = []
# for tok, pos in tagged_tokens:
#     if tok.lower() not in Swords:
#         if pos.startswith('N'):  # noun
#             lemmas.append(lem.lemmatize(tok, pos='n'))
#         elif pos.startswith('J'):  # adj
#             lemmas.append(lem.lemmatize(tok, pos='a'))
#         elif pos.startswith('V'):  # verb
#             lemmas.append(lem.lemmatize(tok, pos='v'))
#         else:
#             lemmas.append(lem.lemmatize(tok))
#
# print(lemmas)

###############make dict
# swords = stopwords.words('english')
# swords.extend(['.', ',', "'", '"', '-', 'else', '$'])
# f = open('./text_data_analysis/scraping_datas/darkknight.txt', 'r')
# content = f.readlines()
# # print(content)
#
# # tokenize
# tokens = []
#
# for line in content:
#     tokenized = nltk.word_tokenize(line)
#     for token in tokenized:
#         if token.lower() not in swords:
#             tokens.append(token)
#
# # POS tagging
# # print(tokens)
# nounlist = []
# adjlist = []
# vlist = []
# for tok, pos in nltk.pos_tag(tokens):
#     if pos.startswith('N'):  # noun
#         nounlist.append(tok.lower())
#     if pos.startswith('J'):
#         adjlist.append(tok.lower())
#     if pos.startswith('V'):
#         vlist.append(tok.lower())
#
# ncounts = Counter(nounlist)
# # print(ncounts.most_common(10))
# adjcounts = Counter(adjlist)
# # print(adjcounts.most_common(10))
# vcounts = Counter(vlist)
# # print(vcounts.most_common(10))
#
# corpus = nltk.Text(tokens)
# # print(len(corpus.tokens))
# # print(len(set(corpus.tokens)))

#######visualization

# swords = stopwords.words('english')
# swords.append('else')
# f = open('./text_data_analysis/scraping_datas/darkknight.txt', 'r')
# content = f.readlines()
#
# # tokenize
# tokens = []
#
# for line in content:
#     tokenized = nltk.word_tokenize(line)
#     for token in tokenized:
#         if token.lower() not in swords:
#             if re.match('^[a-zA-Z]+', token):  # remove special characters
#                 tokens.append(token)
#
# corpus = nltk.Text(tokens)
# # print(corpus.tokens)
# count = Counter(corpus)
# # print(count)
#
# plt.figure(figsize=(10, 3))
# plt.title('Top 25words')
# # corpus.plot(25)
# # print(count.most_common(25))
# plt.bar([x[0] for x in count.most_common(25)], [x[1] for x in count.most_common(25)])
# plt.xticks(rotation=90)
# plt.show()
#
# # print(corpus.similar('batman'))
# # print(corpus.collocations())
#


####################### scikit learn practice
# from sklearn import datasets, model_selection, linear_model, metrics
#
# data = datasets.load_boston()  # boston house price data
# # print(data.keys())
# # print(data.DESCR)
#
# x_data = data['data']
# y_data = data['target']
# x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.3)
#
# model = linear_model.LinearRegression()
#
# model.fit(x_train, y_train)
# model.predict(x_test)
# print(metrics.mean_squared_error(model.predict(x_test), y_test))

########################## calculate cosine similarity in movie reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('./text_data_analysis/scraping_datas/shawshank.txt', 'r')
contents = f.readlines()
first_movie = ' '.join(contents)

f = open('./text_data_analysis/scraping_datas/godfather.txt', 'r')
contents = f.readlines()
second_movie = ' '.join(contents)

f = open('./text_data_analysis/scraping_datas/inception.txt', 'r')
contents = f.readlines()
third_movie = ' '.join(contents)

corpus = [first_movie, second_movie]
sec_corpus = [first_movie, third_movie]
all_together = [first_movie, second_movie, third_movie]

vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(corpus).todense()
# todense() : there are so many zero values, so 'fit_transform' originally saves values except zero values as like a coordinates(x:column, y:rows, value) to make memory usage lower. But todense() makes a matrix that includes zero values. It used only in small datasets.
# If we don't use todense(), it returns a csr matrix
# print(x)

similarity = cosine_similarity(x[0], x[1])  # shawshank, godfather
# print(similarity)  # 0.9437827 => similar!

x = vectorizer.fit_transform(sec_corpus).todense()  # shawshank, inception
similarity = cosine_similarity(x[0], x[1])  # 0.19704257
# print(similarity)

x = vectorizer.fit_transform(all_together).todense()
# fs_sim, ft_sim, st_sim = cosine_similarity(x[0], x[1]), cosine_similarity(x[0], x[2]), cosine_similarity(x[1], x[2])
# f : shawshank, s : godfather, t : incention

# print(f'fs sim : {fs_sim}')
# print(f'ft sim : {ft_sim}')
# print(f'st sim : {st_sim}')

# cosine similarity as one row X the other rows
# cs = cosine_similarity(x[0], x).T  # without .T : 1X3, with .T : 3X1 (transpose)
# print(cs.shape)  # 0: shawshank & shawshank, 1: shawshank & godfather, 2: shawshank & inception

# each row X all rows
cs = cosine_similarity(x, x)  # 3X3
# print(cs)

res = pd.DataFrame(cs)
res.columns = ['shawshank', 'godfather', 'inception']
res.index = ['shawshank', 'godfather', 'inception']
# res['movie name'] = ['shawshank', 'godfather', 'inception']
# res.sort_values(by='shawshank', inplace=True)

# print(res)

plt.figure(figsize=(5, 5))
sns.heatmap(res, annot=True, fmt='f', linewidth=5, cmap='RdYlBu')
# sns.set(font_scale=0.5)
plt.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
plt.show()
