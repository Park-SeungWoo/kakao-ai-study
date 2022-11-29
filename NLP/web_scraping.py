import konlpy
from konlpy.tag import Okt, Kkma
from bs4 import BeautifulSoup

k = Kkma()
print(k.nouns(u'버터 맥주는 풍미가 모두 다르다'))
