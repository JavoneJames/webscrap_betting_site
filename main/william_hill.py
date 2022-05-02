from pickle import dump as save_data
from sys import exit as terminate_program
from time import sleep as prog_sleep
from pandas import DataFrame
from selenium.webdriver.common.by import By

import web_connection_module
from web_connection_module import SetupScraper


class WilliamHill(SetupScraper):

    def __init__(self):
        super().__init__(
            website_url='https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match-betting')

    def established_connection(self):
        self._driver.get(self._website_url)
        cookie_button = self._driver.find_element(by=By.CLASS_NAME, value="cookie-disclaimer__button")
        cookie_button.click()
        prog_sleep(1)
        self.scroll_to_page_bottom()
        prog_sleep(1)
        self.get_fixtures()
        self.write_data_to_file()
        terminate_program(1)

    def scroll_to_page_bottom(self):
        return self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_fixtures(self):
        matches = self._driver.find_elements(by=By.CSS_SELECTOR,
                                            value="#dml > div > div.dml-page-loader.dml-page-loader--pb > section:nth-child(n+1) > div > div > article:nth-child(n+2) > div.sp-o-market__title > a > span")
        odds = self._driver.find_elements(by=By.CSS_SELECTOR,
                                         value="#dml > div > div.dml-page-loader.dml-page-loader--pb > section:nth-child(n+1) > div > div > article:nth-child(n+2) > section")
        for match in matches:
            self._listofteams.append(match.text)
        for odd in odds:
            self._listofOdds.append(odd.text)
        self._driver.quit()

    def write_data_to_file(self):
        dict_list = {'Teams': self._listofteams, 'Odds': self._listofOdds}
        test_table = DataFrame.from_dict(dict_list)
        with open(file='./files/william', mode='wb') as file:
            save_data(obj=test_table, file=file)
        print(test_table)

    def end_script(self):
        self._driver.quit()
        terminate_program(1)
