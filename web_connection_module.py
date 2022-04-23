from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class ConnectToWebsite:

    def __init__(self):
        self.website_url = 'https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match' \
                           '-betting '
        self.chrome_options = Options()
        # chrome_options.binary_location = browser_location
        self.chrome_options.add_argument("--headless")  # Ensure GUI is off
        self.chrome_options.add_argument("--no-sandbox")
        self.chromedriver_path = './chromedriver'
        self.webdriver_service = Service(self.chromedriver_path)
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.chrome_options)

    def established_connection(self):
        self.driver.get(self.website_url)
        cookie_button = self.driver.find_element(by=By.CLASS_NAME, value="cookie-disclaimer__button")
        cookie_button.click()
        self.get_epl_fixtures()

    def get_epl_fixtures(self):
        epl_section = self.driver.find_element(by=By.XPATH, value="//*[@id=\"dml\"]/div/div[2]/section[1]")
        row_events = epl_section.find_elements(by=By.XPATH,
                                               value="//*[@id=\"dml\"]/div/div[2]/section[1]/div/div/article")
        self.extract_team_names_and_odds(row_events)
        self.driver.quit()

    @staticmethod
    def extract_team_names_and_odds(row_events):
        for row in row_events:
            teams_playing = row.find_elements(by=By.CLASS_NAME, value="sp-betName")
            team_odds = row.find_elements(by=By.CLASS_NAME, value="sp-o-market__buttons")
            for fixture in teams_playing:
                print(fixture.text)
            for odds in team_odds:
                print(odds.text)
