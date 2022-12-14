from fp.fp import FreeProxy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class Webdriver_options:

    @staticmethod
    def get_random_ip():
        proxy = FreeProxy(country_id=['US'], rand=True, anonym=True).get()
        ip = proxy.split("://")[1]
        return ip

    @staticmethod
    def get_random_user_agent():
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        return user_agent_rotator.get_random_user_agent()

    @staticmethod
    def chromedriver_path():
        return '/home/denis/Documents/Python/Chromedriver/chromedriver'

    @staticmethod
    def configuration():
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_experimental_option('useAutomationExtension', False)
        # chrome_options.add_argument(f'--proxy-server=%{Webdriver_options.get_random_ip()}')
        # chrome_options.add_argument(f"user-agent={Webdriver_options.get_random_user_agent()}")
        # webdriver.DesiredCapabilities.CHROME['proxy'] = {
        #     "httpProxy": Webdriver_options.get_random_ip(),
        #     "ftpProxy": Webdriver_options.get_random_ip(),
        #     "sslProxy": Webdriver_options.get_random_ip(),
        #     "noProxy": None,
        #     "proxyType": "MANUAL",
        #     "autodetect": False
        # }
        return chrome_options
