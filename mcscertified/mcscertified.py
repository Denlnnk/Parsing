from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Webdriver_folder.Webdriver_options import Webdriver_options
import time


class MCScertified:

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                       options=Webdriver_options.configuration())
        self.url = url
        self.elements_info = []

    def get_data(self):
        self.driver.get(self.url)
        time.sleep(6)

        self.driver.find_element(By.ID, 'msw-show-filters').click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="msw-result-filters"]/div[1]/div[1]/div[1]/label').click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="msw-installer-filter-apply"]'))).click()

        select = Select(self.driver.find_element(By.XPATH, '//*[@id="msw-show-nearest-select"]'))
        select.select_by_visible_text('50')
        time.sleep(7)

        all_elements = self.driver.find_elements(By.CLASS_NAME, 'msw-list-view-item')

        for element in all_elements[:1]:
            element.find_element(By.CLASS_NAME, 'msw-list-view-arrow.down').click()

            product_name = element.find_element(By.XPATH, './/div[1]/div[1]/div[5]').text
            model_number = element.find_element(By.XPATH, './/div/div[1]/div[2]/div[2]').text
            manufacturer = element.find_element(By.XPATH, './/div/div[1]/div[1]/div[2]').text
            technology = element.find_element(By.XPATH, './/div/div[1]/div[2]/div[5]').text
            certification_body = element.find_element(By.XPATH, './/div/div[1]/div[3]/div[2]').text
            website = element.find_element(By.XPATH, './/div/div[1]/div[3]/div[5]/a').get_attribute('href')
            certification_period = element.find_element(By.XPATH, './/div[1]/div[4]/div[2]').text
            current_certification_status = element.find_element(By.XPATH, './/div[1]/div[4]/div[5]').text

            tbody = element.find_element(By.XPATH, './/table/tbody')
            print(tbody)



mcs = MCScertified('https://mcscertified.com/product-directory/')
mcs.get_data()
