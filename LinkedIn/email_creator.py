import time
import random
import string
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from Webdriver_folder.Webdriver_options import Webdriver_options


class Email:

    def __init__(self):
        self.driver = ''
        self.url = 'http://protonmail.com/signup'
        self.username = ''
        self.password = ''

    @staticmethod
    def random_string_digits(string_length=13):
        # Generate a random string of letters and digits
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(string_length))

    def create_email(self):
        self.driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                       options=Webdriver_options.configuration())

        rng_username = self.random_string_digits(13)
        rng_password = self.random_string_digits(15)

        self.driver.get(self.url)
        time.sleep(10)

        self.driver.find_element(
            By.XPATH,
            '//*[@id="gatsby-focus-wrapper"]/main/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/a'
        ).click()
        time.sleep(6)

        self.driver.switch_to.frame(0)
        time.sleep(3)

        self.driver.find_element(By.ID, 'email').send_keys(rng_username)
        time.sleep(1)

        self.driver.switch_to.default_content()
        time.sleep(1)

        self.driver.find_element(By.ID, 'password').send_keys(rng_password)
        time.sleep(1)

        self.driver.find_element(By.ID, 'repeat-password').send_keys(rng_password)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button').click()
        time.sleep(6)

        print('\033[31m' + "Please finish verification" + '\033[0m')

        verification_done = input('\033[31m' + "Hit 'y' when verification is complete" + '\033[0m')
        if verification_done == 'y':
            time.sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/main/div[2]/form/button').click()
        else:
            pass
        print('\033[31m' + "Your New Email Adress is: ", rng_username, "@protonmail.com", sep='' + '\033[0m')
        print('\033[31m' + "Your New Email Password is: " + '\033[0m', rng_password)
        self.username = rng_username
        self.password = rng_password

    def save_to_scv(self):
        csv_data = [[self.username + '@protonmail.com', self.password]]
        with open('static/list.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csv_data)
        csvFile.close()
        print('\033[31m' + 'Great! We added you account details to the table.' + '\033[0m')

