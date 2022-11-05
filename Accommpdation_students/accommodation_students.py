from selenium import webdriver
from Webdriver_folder.Webdriver_options import Webdriver_options


driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                          options=Webdriver_options.configuration())
driver.get('http://www.google.com')

driver.close()
