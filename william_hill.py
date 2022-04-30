from sys import exit as terminate_program
from time import sleep as prog_sleep

import pandas
from selenium.webdriver.common.by import By
from web_connection_module import SetupScraper
from pandas import DataFrame, set_option
import numpy as np


class WilliamHill(SetupScraper):

    def __init__(self):
        super().__init__(
            website_url='https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match-betting')

    def established_connection(self):
        self.driver.get(self.website_url)
        cookie_button = self.driver.find_element(by=By.CLASS_NAME, value="cookie-disclaimer__button")
        cookie_button.click()
        self.scroll_to_page_bottom()
        prog_sleep(.5)
        self.get_fixtures()

    def scroll_to_page_bottom(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_fixtures(self):
        matches = self.driver.find_elements(by=By.CSS_SELECTOR,
                                            value="#dml > div > div.dml-page-loader.dml-page-loader--pb > section:nth-child(n+1) > div > div > article:nth-child(n+2) > div.sp-o-market__title > a > span")
        odds = self.driver.find_elements(by=By.CSS_SELECTOR,
                                         value="#dml > div > div.dml-page-loader.dml-page-loader--pb > section:nth-child(n+1) > div > div > article:nth-child(n+2) > section")
        for count, match in enumerate(matches, start=1):
            self.listofteams.append(match.text)
        for counter, odd in enumerate(odds, start=1):
            self.listofOdds.append(odd.text)
        self.driver.quit()
        dict_list = {'Teams': self.listofteams, 'Odds': self.listofOdds}
        test_table = DataFrame.from_dict(dict_list)
        print(test_table)
        terminate_program(1)

    def end_script(self):
        self.driver.quit()
        terminate_program(1)
