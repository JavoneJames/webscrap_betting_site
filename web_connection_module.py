from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class ConnectToWebsite:

    def __init__(self):
        website = 'https://sports.williamhill.com/betting/en-gb'
        chrome_options = Options()
        # chrome_options.binary_location = browser_location
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")
        chromedriver_path = './chromedriver'
        webdriver_service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        driver.get(website)
        if driver.service.process is not None:
            print("connected")
        driver.quit()
