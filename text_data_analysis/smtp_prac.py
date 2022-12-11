import smtplib
from email.mime.text import MIMEText

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

import json
SECURES = json.load(open('./keys.json', 'r'))
GOOGLE_APP_PW = SECURES['GOOGLE_APP_PASSWORD']
EMAIL_ADDR = SECURES['GMAIL_ADDR']


def send_mail(sender, receiver, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # 465: port number
    smtp.login(sender, GOOGLE_APP_PW)

    msg = MIMEText(msg)  # make a mail obj
    msg['Subject'] = 'Product is available'  # set title

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def wadiz_check_is_soldout(product_code, price_want):
    try:
        web = urlopen('https://www.wadiz.kr/web/campaign/detail/' + str(product_code))
        dom = BeautifulSoup(web, 'html.parser')
        button_elems = dom.find('div', {'class': 'wd-ui-gift'}).find_all('button')
        target_elem = ''
        for button_elem in button_elems:
            price = button_elem.find('dt').get_text().strip()[:-4].replace(',', '')
            if price == price_want:
                target_elem = button_elem
        if target_elem == '':
            raise Exception('No element founded, Please check information again')
        is_soldout = ('soldout' in target_elem.attrs['class'])
        return is_soldout
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    product_code = 76816
    want_price = '398000'
    while True:
        is_soldout = wadiz_check_is_soldout(product_code, want_price)
        if not is_soldout:
            send_mail(EMAIL_ADDR, EMAIL_ADDR, f'{product_code} is available https://www.wadiz.kr/web/campaign/detail/{product_code}')
            print('mail sent')
            break
        else:
            print('not available yet', time.time())
        time.sleep(300)


"""
smtplib
smtp => simple mail transfer protocol
"""