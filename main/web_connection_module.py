from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as web_service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


class SetupScraper(ABC):
    def __init__(self, website_url):
        self._website_url = website_url
        self.__chrome_options = Options()
        # self.__chrome_options.browser_version = '100.0.4896.127'
        self.__chrome_options.headless = True
        self.__chrome_options.add_argument('window-size=1920x1080')
        self.__chrome_options.page_load_strategy = 'normal'  # do not change load strategy from normal to eager/none
        self.__chrome_options.add_argument("--no-sandbox")
        # self._webdriver_service = Service()
        # self.__webdriver_service.path = r'../resources/chromedriver'
        # self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.chrome_options)
        self._driver = webdriver.Chrome(service=web_service(ChromeDriverManager(version='latest',
        chrome_type=ChromeType.CHROMIUM).install()), options=self.__chrome_options)
        self._driver.maximize_window()
        self._driver.implicitly_wait(60)
        self._listofteams = []
        self._listofOdds = []

    @abstractmethod
    def established_connection(self):
        pass

    @abstractmethod
    def get_fixtures(self):
        pass

    @abstractmethod
    def write_data_to_file(self):
        pass
