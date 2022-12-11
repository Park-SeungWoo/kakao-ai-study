from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup

import pandas as pd

pd.set_option('expand_frame_repr', False)

import time

'''******decorator******'''


def driver_close(func):
    def wrapper(*args, **kwargs):
        driver = args[0]
        result = func(*args, **kwargs)
        driver.close()
        driver.quit()
        return result

    return wrapper


def paging(get_infos):
    def wrapper(*args, **kwargs):
        driver = args[0]
        infos_every_page = []  # saves all datas from each page
        while True:
            try:
                infos_every_page.extend(get_infos(*args, **kwargs))  # get tour lists
                paging_elem = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.CLASS_NAME, 'pageNumBox')))  # wait until paging box loaded, and save element
                next_btn_elem = paging_elem.find_element_by_class_name('nextBtn')  # find nextBtn in paging box
                next_btn_elem.click()
                print('new page loading')
            except NoSuchElementException:  # selenium.common.exceptions  (if no elements => last page)
                print('paging process is done')
                break
            except BaseException as e:  # other exceptions
                print("something's wrong in paging decorator")
                print(e)
                break

        return infos_every_page

    return wrapper


'''******methods******'''


@paging
def get_tour_infos_selenium(driver):  # using selenium
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[2]/ul')))
    tour_lists_elem = driver.find_elements_by_xpath(
        '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[2]/ul/li[*]')  # get list elements one by one
    products = []
    for tour_elem in tour_lists_elem:
        # tour_infos = tour_elem.text.split('\n')  # All texts in tour lists
        """
        text datas
        title: title
        price: price
        starting_dates: able dates to start tour
        able_sd_from: the first date which is able to start the tour
        able_sd_to: the last date which is able to start the tour
        """
        title = tour_elem.find_element_by_class_name('infoTitle').text
        price = tour_elem.find_element_by_class_name('infoPrice').text[4:-2]
        starting_dates = tour_elem.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li/div/div[2]/div[3]/div[1]/p[2]').text.split(
            ':')[1].strip()
        able_sd_from = starting_dates.split('~')[0]
        able_sd_to = starting_dates.split('~')[1]

        """
        image data
        product_img_src: Image that represents that tour
        """
        product_img_src = tour_elem.find_element_by_tag_name('img').get_attribute('src')

        # wrap it as a list
        products.append([title, price, able_sd_from, able_sd_to, product_img_src])
    print('data scraping finished in this page')
    return products  # return a structured information list in this page


# same as above, but using bs4 not selenium
@paging
def get_tour_infos_bs(driver):  # using bs4
    DOM = BeautifulSoup(driver.page_source, 'html.parser')
    tour_lists_elem = DOM.find('div', {'class': "overseaTravel"}).find('ul', {'id': 'boxList'}).find_all('li', {
        'class': 'boxItem'})
    products = []
    for tour_elem in tour_lists_elem:
        title = tour_elem.find('h5', {'class': 'infoTitle'}).get_text()
        price = tour_elem.find('div', {'class': 'infoPrice'}).find('strong').get_text()
        starting_date = tour_elem.find_all('p', {'class': 'info'})[1].get_text().split(':')[1].strip()
        able_sd_from = starting_date.split('~')[0]
        able_sd_to = starting_date.split('~')[1]
        product_img_src = tour_elem.find('img').attrs['src']
        products.append([title, price, able_sd_from, able_sd_to, product_img_src])
    return products  # return a structured information list in this page


@driver_close
def scraping_tour_lists(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[3]/div/button'))).click()  # click more infos
    return get_tour_infos_bs(driver)  # get tour lists, {options: [bs4, selenium]}


'''******main******'''
if __name__ == '__main__':
    URL = 'https://search-travel.interpark.com/search?q={}'
    QUERY = '일본'

    option = webdriver.ChromeOptions()
    option.add_experimental_option('prefs', {'intl.accept_languages': 'ko'})
    driver = webdriver.Chrome(executable_path=r'./text_data_analysis/Chrome_driver/chromedriver', options=option)
    driver.get(URL.format(QUERY))

    products = scraping_tour_lists(driver)
    products_df = pd.DataFrame(products, columns=['Title', 'Price', 'Able from', 'Able to', 'Image'])  # as a df
    products_df['Price'] = products_df['Price'].apply(lambda x: int(x.replace(',', '')))
    print(products_df.head(10))
    products_df.sort_values(by='Price', inplace=True)
    print(products_df)
    print(products_df[products_df['Price'] < 1000000])
    print(products_df[ (products_df['Title'].str.contains('오사카')) & (products_df['Price'] < 1000000) ])