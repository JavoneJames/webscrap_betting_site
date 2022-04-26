from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class SetupScraper:
    def __init__(self, website_url):
        self.website_url = website_url
        self.chrome_options = Options()
        self.chrome_options.browser_version = '100.0.4896.127'
        self.chrome_options.headless = True
        self.chrome_options.page_load_strategy = 'normal'  # do not change load strategy from normal to eager/none
        self.chrome_options.add_argument("--no-sandbox")
        self.webdriver_service = Service()
        self.webdriver_service.path = r'../sites/chromedriver'
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.chrome_options)
        self.driver.implicitly_wait(30)
        self.listofteams = []
        self.listofOdds = []
