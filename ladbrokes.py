from web_connection_module import SetupScraper
from sys import exit as terminate_program
from time import sleep as prog_sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Ladbrokes(SetupScraper):
    def __init__(self):
        super().__init__(website_url="https://sports.ladbrokes.com/sport/football/matches/today")

    def established_connection(self):
        self.driver.get(self.website_url)
        print(self.driver.title)
        self.driver.maximize_window()
        self.get_fixtures()

    def get_fixtures(self):
        row_events = self.driver.find_elements(by=By.CSS_SELECTOR, value="#content > sport-main-component > "
                                                                         "div.page-inner > div > sport-matches-page > "
                                                                         "sport-matches-tab > accordion:nth-child(n+5) "
                                                                         "> header > div.accordion-left-side")
        print(len(row_events))
        for row in row_events:
            print(row.text)
            row.click()
            prog_sleep(.5)
        self.end_script()

    def end_script(self):
        self.driver.quit()
        terminate_program(1)
