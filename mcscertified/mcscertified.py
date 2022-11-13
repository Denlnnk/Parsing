import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Webdriver_folder.Webdriver_options import Webdriver_options
import time
from datetime import date


class Mcscertified:

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                       options=Webdriver_options.configuration())
        self.url = url
        self.elements_info = []
        self.current_date = date.today()

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

        while True:
            time.sleep(10)
            try:
                self.driver.find_element(By.CLASS_NAME, 'paginate_button next disabled')
            except selenium.common.exceptions.NoSuchElementException as ex:
                pass
            else:
                break
            all_elements = self.driver.find_elements(By.CLASS_NAME, 'msw-list-view-item')

            all_elements_len = 0
            for element in all_elements:
                element.find_element(By.CLASS_NAME, 'msw-list-view-arrow.down').click()

                product_name = element.find_element(By.XPATH, './/div[1]/div[1]/div[5]').text
                model_number = element.find_element(By.XPATH, './/div/div[1]/div[2]/div[2]').text
                manufacturer = element.find_element(By.XPATH, './/div/div[1]/div[1]/div[2]').text
                technology = element.find_element(By.XPATH, './/div/div[1]/div[2]/div[5]').text
                certification_body = element.find_element(By.XPATH, './/div/div[1]/div[3]/div[2]').text
                website = element.find_element(By.XPATH, './/div/div[1]/div[3]/div[5]/a').get_attribute('href')
                certification_period = element.find_element(By.XPATH, './/div[1]/div[4]/div[2]').text
                current_certification_status = element.find_element(By.XPATH, './/div[1]/div[4]/div[5]').text

                self.elements_info.append({
                    'Manufacturer': manufacturer,
                    'Product_name': product_name,
                    'Model_number': model_number,
                    'Technology': technology,
                    'Certification_body': certification_body,
                    'Website': website,
                    'Certification_period': certification_period,
                    'Current_certification_status': current_certification_status
                })
            all_elements_len += len(all_elements)
            print(f'Collected {all_elements_len} items')
            self.driver.find_element(By.XPATH, '//*[@id="ProductResultsTableAll_next"]').click()
        self.driver.quit()

    def save_to_scv(self):
        df = pd.DataFrame(self.elements_info)
        df.to_csv(f'{self.current_date}.csv', index=False)
        print('Saved to csv')


def main():
    mcs = Mcscertified('https://mcscertified.com/product-directory/')
    mcs.get_data()
    mcs.save_to_scv()


if __name__ == '__main__':
    main()
