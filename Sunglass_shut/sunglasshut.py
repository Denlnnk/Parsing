import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from Webdriver_folder.Webdriver_options import Webdriver_options

baseurl = 'https://www.sunglasshut.com'
headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def product_links():
    all_links = []
    for x in range(1, 2):
        response = requests.get(f'https://www.sunglasshut.com/uk/mens-sunglasses?currentPage={x}',
                                headers=headers).content
        bs4 = BeautifulSoup(response, 'lxml')

        content_info = bs4.findAll('div', class_='sgh-col sm:w-1/3 w-1/2')

        for info in content_info:
            all_links.append(baseurl + info.find('a')['href'])
        print(f'Collected {x} pages')

    return all_links


def result_info(links: list):
    products_info = []
    count = 0
    for link in links:
        count += 1
        response = requests.get(link, headers=headers).content
        bs4 = BeautifulSoup(response, 'lxml')

        driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                  options=Webdriver_options.configuration())
        driver.get(link)

        size_button = driver.find_element(By.XPATH, './/*[@id="openSizesPopupBtn"]')
        size_button.click()
        time.sleep(3)
        size = driver.find_element(By.XPATH, './/*[@id="757058"]/a/span[1]').text.strip()
        print(size)
        driver.quit()
        products_info.append({
            'name': bs4.find('p', class_='sgh-pdp__brand-name').text.strip(),
            'price': bs4.find('span', class_='sale-price price').text.strip(),
            'colors': bs4.find('span', class_='sgh-pdp__filter-value sgh-pdp__filter-value--polarized').text.strip(),
            'size': size
        })
        print(f'Collected {count} products')

    return products_info


def to_scv(info: list):
    df = pd.DataFrame(info)
    df.to_csv('sunglass.csv')


product_links = product_links()
product_info = result_info(product_links)
# to_scv(product_info)
