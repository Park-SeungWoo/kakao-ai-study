from konlpy.tag import Kkma
from bs4 import BeautifulSoup
from urllib.request import urlopen

# word = 'happiness'
# url = 'https://alldic.daum.net/search.do?q='
# web = urlopen(url + word)
# web_page = BeautifulSoup(web, 'html.parser')
# print(web_page)

# print(web_page.find('p').attrs['id'])
# for p_tag in web_page.find_all('p'):
#     print(p_tag.get_text())

# print(web_page.find('span', {'class': 'txt_emph1'}).get_text())

# for span_tag in web_page.find_all('span', {'class': 'txt_search'}):
#     print(span_tag.get_text())

# words = ['love', 'happy', 'baby', 'like', 'soul']

# for word in words:
#     web = urlopen(url + word)
#     web_page = BeautifulSoup(web, 'html.parser')
#     for definition in web_page.find_all('span', {'class': 'txt_search'}):
#         print(definition.get_text())

################################## movie page
###############title
movie_url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code='
movie_code = '208077'

web = urlopen(movie_url + movie_code)
webpage = BeautifulSoup(web, 'html.parser')

title = webpage.find('h3', {'class': 'h_movie'}).find('a').get_text()
plots = webpage.find('p', {'class': 'con_tx'}).get_text()
# print(title)
# print(plots)

##############director, actor
director_url = 'https://movie.naver.com/movie/bi/mi/detail.naver?code='
web = urlopen(director_url + movie_code)
webpage = BeautifulSoup(web, 'html.parser')

director = webpage.find('div', {'class': 'dir_product'}).find('a', {'class': 'k_name'}).get_text()
# print(director)
actors = []
for div_tag in webpage.find_all('div', {'class': 'p_info'}):
    actor = div_tag.find('a', {'class': 'k_name'})
    actors.append(actor.get_text())

# print(actors)

############reviews
# review_url = 'https://movie.naver.com/movie/bi/mi/review.naver?code='
# web = urlopen(review_url + movie_code)
# webpage = BeautifulSoup(web, 'html.parser')

# review_titles = []
# for li_tag in webpage.find('ul', {'class': 'rvw_list_area'}).find_all('li'):
#     title = li_tag.find('strong').get_text()
#     review_titles.append(title)

# print(review_titles)

######################get all reviews, check out all pages
# review_titles = []
# page = 1
# while True:
#     review_url = 'https://movie.naver.com/movie/bi/mi/review.naver?code=' + movie_code + '&page=' + str(page)
#     web = urlopen(review_url)
#     webpage = BeautifulSoup(web, 'html.parser')
#     # If it is the last page, there's not a 'a_tag' that has a class named 'pg_next'
#     is_not_last = webpage.find('div', {'class': 'paging'}).find_all('a', {'class': 'pg_next'})
#
#     for li_tag in webpage.find('ul', {'class': 'rvw_list_area'}).find_all('li'):  # get all reviews' titles.
#         title = li_tag.find('strong').get_text()
#         review_titles.append(title)
#
#     if not is_not_last:  # If it is the last review page, break
#         break
#     page += 1

# print(review_titles)

########################### blog data
error_urls = []
blog_url = 'https://brunch.co.kr/@imagineer/'
blog_page = 1
while True:
    try:
        web = urlopen(blog_url + str(blog_page))
        source = BeautifulSoup(web, 'html.parser')
        is_not_last_article = source.find('div', {'class': 'wrap_page_article'}).find('a', {'class': 'link_next'})  # find last article

        with open('./NLP/scrapping_datas/blog_content.txt', 'a', encoding='utf-8') as f:  # get content and save
            f.write('In' + blog_url + str(blog_page) + '\n')
            content_all = source.find('div', {'class': 'wrap_body'}).find_all()
            for content in content_all:
                f.write(content.get_text() + '\n')

        if not is_not_last_article:  # if last, break
            break
        print(str(blog_page) + ' is good')
        blog_page += 1
    except:
        error_urls.append(blog_url + str(blog_page))  # If the page doesn't exist
        print(str(blog_page) + ' is failed')
        blog_page += 1
print(error_urls)
###### have to learn about bypassing http request limits in web scraping.