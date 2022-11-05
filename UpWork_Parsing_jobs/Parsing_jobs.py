import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from Webdriver_folder.Webdriver_options import Webdriver_options

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

baseurl = 'https://www.upwork.com/nx/jobs/search/?q=data%20scraping&sort=recency&contractor_tier=1&proposals=0-4,5-9'


def get_data():
    driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                              options=Webdriver_options.configuration())
    page_html = driver.get(baseurl)

    time.sleep(3)

    with open('content_page', 'w') as file:
        file.write(driver.page_source)


def main():
    get_data()


if __name__ == '__main__':
    main()
