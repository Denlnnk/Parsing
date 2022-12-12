from selenium import webdriver
from Webdriver_folder.Webdriver_options import Webdriver_options


class LinkedIn_profiles:

    def __init__(self, location: str, job_position: str):
        self.username = ''
        self.password = ''
        self.location = location
        self.job_position = job_position
