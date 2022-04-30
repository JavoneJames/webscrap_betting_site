from web_connection_module import SetupScraper
from sys import exit as terminate_program
from time import sleep as prog_sleep
from selenium.webdriver.common.by import By


class Ladbrokes(SetupScraper):
    def __init__(self):
        super().__init__(website_url="https://sports.ladbrokes.com/sport/football/matches/today")

    def established_connection(self):
        self.webdriver_service.start()
        self.driver.get(self.website_url)
        self.open_closed_tabs()

    def open_closed_tabs(self):
        row_events = self.driver.find_elements(by=By.CSS_SELECTOR, value="#content > sport-main-component > div.page-inner > div > "
                                                                         "sport-matches-page > sport-matches-tab > accordion:nth-child(n+5) "
                                                                         "> header > div.accordion-left-side")
        for row in row_events:
            row.click()
            prog_sleep(.5)
        self.get_fixtures()

    def get_fixtures(self):
        matches = self.driver.find_elements(by=By.CSS_SELECTOR,
                                            value="#content > sport-main-component > div.page-inner > div > sport-matches-page > sport-matches-tab > "
                                                  "accordion:nth-child(n+2) > accordion-body > div > odds-card-component > odds-card-sport > div > "
                                                  "div.sport-card-content > div.sport-card-left > div")
        odds = self.driver.find_elements(by=By.CLASS_NAME, value="sport-card-btn-content")
        for match in matches:
            self.listofteams.append(match.text.replace("\n", " v "))
        for odd in odds:
            self.listofOdds.append(tuple(odd.text.split("\n")))
        dict_from_list = dict(zip(self.listofteams, self.listofOdds))
        print(dict_from_list)
        self.end_script()

    def end_script(self):
        self.driver.quit()
        terminate_program(1)
