from sys import exit as terminate_program
from time import sleep as prog_sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ConnectToWebsite:

    def __init__(self):
        self.website_url = 'https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match' \
                           '-betting '
        self.chrome_options = Options()
        self.chrome_options.browser_version = '100.0.4896.127'
        self.chrome_options.headless = True
        self.chrome_options.page_load_strategy = 'normal'  # do not change load strategy from normal to eager/none
        self.chrome_options.add_argument("--no-sandbox")
        self.webdriver_service = Service()
        self.webdriver_service.path = r'./chromedriver'
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.chrome_options)
        self.listofteams = []
        self.listofOdds = []

    def established_connection(self):
        self.driver.get(self.website_url)
        prog_sleep(0.5)  # sleep for a couple seconds after accessing site - reduce spam attempts
        cookie_button = self.driver.find_element(by=By.CLASS_NAME, value="cookie-disclaimer__button")
        cookie_button.click()
        self.driver.maximize_window()
        prog_sleep(0.5)
        self.scroll_to_page_bottom()
        prog_sleep(0.5)
        self.get_epl_fixtures()

    def scroll_to_page_bottom(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_epl_fixtures(self):
        row_events = self.driver.find_elements(by=By.XPATH, value="//*[@id=\"dml\"]/div/div[2]/section/div/div/article")
        for row in row_events:
            teams_playing = row.find_elements(by=By.CLASS_NAME, value="sp-betName")
            team_odds = row.find_elements(by=By.CLASS_NAME, value="sp-o-market__buttons")
            for fixtures in teams_playing:
                self.listofteams.append(fixtures.text)
            for odds in team_odds:
                self.listofOdds.append(tuple(odds.text.split('\n')))
        dict_from_list = dict(zip(self.listofteams, self.listofOdds))
        print(dict_from_list)
        self.end_script()

    def end_script(self):
        self.driver.quit()
        terminate_program(1)
