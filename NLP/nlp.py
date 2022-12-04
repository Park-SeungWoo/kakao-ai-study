import nltk  # doesn't have ko nlp
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import re

# sentence = 'NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.'
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
# f = open('./NLP/scraping_datas/moviereview.txt', 'r')
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
# f = open('./NLP/scraping_datas/darkknight.txt', 'r')
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
# f = open('./NLP/scraping_datas/darkknight.txt', 'r')
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


####################### final practice
