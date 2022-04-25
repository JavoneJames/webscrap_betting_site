import WilliamHill
from web_connection_module import SetupScraper
from WilliamHill import WilliamHill

if __name__ == '__main__':
    william = WilliamHill('https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match-betting')
    william.established_connection()
