from requests import get
from pprint import PrettyPrinter
printer = PrettyPrinter()

BASE_URL = "https://livescore-api.com/api-client"
KEY = "CHANGE IT TO YOUR KEY"
SECRET_KEY = "CHANGE IT TO YOUR SECRET KEY"

def fixtures():
    FIXTURES_API = "/fixtures/matches.json?competition_id=60"
    API = BASE_URL + FIXTURES_API + "&key=" + KEY + "&secret=" + SECRET_KEY
    matches = get(API).json()['data']['fixtures']
    matches = list(filter(lambda x: x['home_name'] == "Legia Warszawa" or x['away_name'] == "Legia Warszawa", matches))
    print("NEXT LEGIA WARSZAWA GAMES:")
    for match in matches:
        date = match['date']
        hour = match['time']
        team1 = match['home_name']
        team2 = match['away_name']
        print(f"{team1} - {team2} [{date}, {hour}]")


fixtures()