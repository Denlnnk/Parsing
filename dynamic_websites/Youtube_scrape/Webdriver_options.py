from selenium.webdriver.chrome.options import Options


class Webdriver_options:

    @staticmethod
    def chromedriver_path():
        return '/home/denis/Documents/Python/Chromedriver/chromedriver'

    @staticmethod
    def configuration():
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option("detach", True)
        return chrome_options
