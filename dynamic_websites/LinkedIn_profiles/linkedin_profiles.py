import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Webdriver_folder.Webdriver_options import Webdriver_options


class LinkedIn_profiles:

    def __init__(self, location: str = None, job_position: str = None):
        self.username = ''
        self.password = ''
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
        time.sleep(4)




if __name__ == '__main__':
    linked = LinkedIn_profiles(location='North America')
    linked.parse()
