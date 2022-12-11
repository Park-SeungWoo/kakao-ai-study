import time

from selenium import webdriver
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings('ignore')


def driver_close(func):
    def wrapper(*args, **kwargs):
        driver = args[0]
        func(*args, **kwargs)
        driver.close()
        driver.quit()
    return wrapper


@driver_close
def scroll_page(driver):
    while True:
        last_sh = driver.execute_script('return document.body.scrollHeight')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)  # wait until scroll, page loaded
        new_sh = driver.execute_script('return document.body.scrollHeight')
        if last_sh == new_sh:
            break

    print('scroll finished')


option = webdriver.ChromeOptions()
option.add_experimental_option('prefs', {'intl.accept_languages': 'ko'})
driver = webdriver.Chrome(executable_path=r'./text_data_analysis/Chrome_driver/chromedriver', options=option)

artist = 'whykhaliq'
url = 'https://soundcloud.com/' + artist + '/tracks'

driver.get(url)

scroll_page(driver)
