from bs4 import BeautifulSoup
import requests

import json
SAMPLE_API_KEY = json.load(open('./keys.json', 'r'))["SAMPLE_API_KEY"]
API_KEY = json.load(open('./keys.json', 'r'))["OPEN_API_KEY"]

REQ_URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc'

params = {
    'LAWD_CD': '11690',
    'DEAL_YMD': '202211',
    'serviceKey': API_KEY
}

data_xml = requests.get(REQ_URL, params=params).content
datas = BeautifulSoup(data_xml, 'lxml-xml', from_encoding='euc-kr')

items = datas.find_all('item')

"""
xml: can access each data using tag name like html
"""