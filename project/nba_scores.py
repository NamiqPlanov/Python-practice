from requests import get
from pprint import PrettyPrinter


base_url = 'https://data.nba.net'
json_data = '/prod/v1/today.json'


printer = PrettyPrinter()
def get_links():
   data = get(base_url+json_data).json()
   links = data['links']
   return links



def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(base_url+scoreboard).json()['games']
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print('-----------------------------------------------------------------')
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']}-{away_team['score']}")
        print(f"{clock}-{period['current']}")

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(base_url+stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x:x['name']!='Team', teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    
    for i,team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        abb = team['abbreviation']
        ppg = team['ppg']
        print(f"{i+1}.{name}-{nickname}-{abb}-{ppg}")
       
get_stats()
   


    