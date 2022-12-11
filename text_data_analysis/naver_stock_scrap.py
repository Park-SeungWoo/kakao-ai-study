import requests
from bs4 import BeautifulSoup


def summary(stocks):
    for stock in stocks['stocks']:
        print(f"{stock['name']} : "
              f"현재가 {stock['price']}, "
              f"어제보다 {stock['delta_price']} {'상승' if stock['increased'] else '하락'}, "
              f"백분율 변환 시 {stock['delta_rate']}")

    print(f"어제보다 상승한 종목은 {[s['name'] for s in stocks['increased_stock']]} 입니다.")  # increased_stock: list[dict]
    print(f"어제보다 가장 많이 상승한 종목은 [ {stocks['top_increased_stock']['name']} ({stocks['top_increased_stock']['delta_rate']}) ] 입니다.")


def scraping(url):
    web = requests.get(url).content
    dom = BeautifulSoup(web, 'html.parser', from_encoding='euc-kr')
    table_elem = dom.find('tbody', {'id': '_topItems1'})
    stock_datas = {
        'stocks': [],
        'top_increased_stock': {},
        'increased_stock': [],
        'decreased_stock': []
    }
    for item_elem in table_elem.find_all('tr'):
        stock = dict(name=str, price=str, increased=bool, delta_price=str, delta_rate=str)  # set types of the items
        stock['name'] = item_elem.find('th').get_text()
        prices_elem = item_elem.find_all('td')
        stock['price'] = prices_elem[0].get_text()
        stock['increased'] = True if prices_elem[1].get_text().split(' ')[0] == '상승' else False
        stock['delta_price'] = prices_elem[1].get_text().split(' ')[1]
        stock['delta_rate'] = prices_elem[2].get_text().strip()
        stock_datas['stocks'].append(stock)
        if stock['increased']:
            stock_datas['increased_stock'].append(stock)
        else:
            stock_datas['decreased_stock'].append(stock)

    stock_datas['increased_stock'].sort(key=lambda s: float(s['delta_rate'][1:-1]), reverse=True)
    stock_datas['top_increased_stock'] = stock_datas['increased_stock'][0]
    summary(stock_datas)


url = 'https://finance.naver.com'
scraping(url)