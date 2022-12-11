import requests
from bs4 import BeautifulSoup

import json

def dldl():
    pass

if __name__ == '__main__':
    url = 'https://golmok.seoul.go.kr/stateArea.do'
    post_url = 'https://golmok.seoul.go.kr/region/selectRentalPrice.json'
    post_str_ex = 'stdrYyCd=2022&stdrSlctQu=sameQu&stdrQuCd=2&stdrMnCd=202206&selectTerm=quarter&svcIndutyCdL=CS000000&svcIndutyCdM=all&stdrSigngu=11&selectInduty=1&infoCategory=rent'
    post_dict = {}
    for query in post_str_ex.split('&'):
        query_list = query.split('=')
        key = query_list[0]
        value = query_list[1]
        post_dict[key] = value

    post_res = requests.post(post_url, data=post_dict).content
    res = json.loads(post_res)
    print(res)