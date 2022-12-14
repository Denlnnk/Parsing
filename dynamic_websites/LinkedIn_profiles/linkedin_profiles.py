import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Webdriver_folder.Webdriver_options import Webdriver_options


class LinkedIn_profiles:

    def __init__(self, location: str = None, job_position: str = None):
        self.username = 'denlnnk2014@gmail.com'
        self.password = 'hellomydear12'
        self.liked_url = 'https://www.linkedin.com/'
        self.location = location
        self.job_position = job_position

    def parse(self):
        # Login section
        driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                  options=Webdriver_options.configuration())
        driver.get(self.liked_url)

        driver.find_element(By.ID, 'session_key').send_keys(self.username)
        driver.find_element(By.ID, 'session_password').send_keys(self.password)
        driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button').click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'ember-view.block')))

        # Search section
        driver.get('https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&sid=%3A5U')

        if self.location:
            driver.find_element(
                By.XPATH,
                '//button[@aria-label="Locations filter. Clicking this button displays all Locations filter options."]'
            ).click()
            time.sleep(1)
            input_location = driver.find_element(By.XPATH, '//input[@aria-label="Add a location"]')
            input_location.send_keys(self.location)
            time.sleep(1)
            input_location.send_keys(Keys.ARROW_DOWN)
            input_location.send_keys(Keys.ENTER)
            time.sleep(1)

            driver.find_element(By.XPATH, '//button[@aria-label="Click to start a search"]').click()
            time.sleep(3)

        if self.job_position:
            driver.find_element(By.XPATH, '//button[@aria-label="Click to start a search"]').click()
            time.sleep(2)
            input_job_position = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')
            input_job_position.send_keys(self.job_position)
            time.sleep(1)
            input_job_position.send_keys(Keys.ENTER)


if __name__ == '__main__':
    linked = LinkedIn_profiles(location='United States', job_position='North America')
    linked.parse()
