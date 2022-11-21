import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from Webdriver_folder.Webdriver_options import Webdriver_options


class Linkedin:

    def __init__(self, first_name: str, last_name: str, phone_number: str):
        self.driver = ''
        self.url = 'https://www.linkedin.com/signup/cold-join?trk=guest_homepage-basic_nav-header-join'
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def account_register(self):
        email_info = {}
        with open('static/list.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                email_info = {
                    'email': row[0],
                    'password': row[1]
                }
        self.driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                       options=Webdriver_options.configuration())

        self.driver.get(self.url)
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="email-address"]').send_keys(email_info['email'])
        time.sleep(1)

        self.driver.find_element(By.ID, 'password').send_keys(email_info['password'])
        time.sleep(1)

        self.driver.find_element(By.ID, 'join-form-submit').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(self.first_name)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(self.last_name)
        time.sleep(1)

        self.driver.find_element(By.ID, 'join-form-submit').click()
        time.sleep(4)

        # self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))
        self.driver.switch_to.frame(1)
        time.sleep(3)

        self.driver.find_element(By.ID, 'register-verification-phone-number').send_keys(self.phone_number)
        self.driver.find_element(By.ID, 'register-phone-submit-button').click()

        print('Pls finish verification')
        verification_done = input('\033[31m' + "Hit 'y' when verification is complete" + '\033[0m')
        if verification_done == 'y':
            print('You are logged in')
        else:
            pass
