from web_connection_module import SetupScraper
from sys import exit as terminate_program
from time import sleep as prog_sleep
from selenium.webdriver.common.by import By
from pandas import DataFrame
from pickle import dump as save_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Ladbrokes(SetupScraper):
    def __init__(self):
        super().__init__(website_url="https://sports.ladbrokes.com/sport/football/matches/today")

    def established_connection(self):
        self._driver.get(self._website_url)
        self._driver.save_screenshot("save1.png")
        prog_sleep(.9)
        self.open_closed_tabs()
        self.get_fixtures()
        self.write_data_to_file()
        self.end_script()

    def open_closed_tabs(self):
        row_events = self._driver.find_elements(by=By.CSS_SELECTOR,
                                                value="#content > sport-main-component > div.page-inner > div > sport-matches-page > sport-matches-tab > accordion:nth-child(n+5) > header > div.accordion-left-side")
        for row in row_events:
            prog_sleep(.9)
            row.click()

    def get_fixtures(self):
        matches = self._driver.find_elements(by=By.CSS_SELECTOR,
                                             value="#content > sport-main-component > div.page-inner > div > sport-matches-page > sport-matches-tab > "
                                                   "accordion:nth-child(n+2) > accordion-body > div > odds-card-component > odds-card-sport > div > "
                                                   "div.sport-card-content > div.sport-card-left > div")
        odds = self._driver.find_elements(by=By.CLASS_NAME, value="sport-card-btn-content")
        for match in matches:
            self._listofteams.append(match.text.replace("\n", " v "))
        for odd in odds:
            self._listofOdds.append(odd.text)
        self._driver.quit()

    def write_data_to_file(self):
        dict_from_list = {'Teams': self._listofteams, 'Odds': self._listofOdds}
        test_table = DataFrame.from_dict(data=dict_from_list)
        with open(file='./files/ladbrokes', mode='wb') as file:
            save_data(obj=test_table, file=file)
        print(test_table)

    def end_script(self):
        self._driver.quit()
        terminate_program(1)
