import requests
import json
from input import *
from Match import Match


new_matches = []


def get_competition_id():
    response = requests.get('https://api.football-data.org/v2/competitions/', headers=HEADER)
    parsed_response = json.loads(response.text)
    for competition in parsed_response['competitions']:
        if competition['area']['name'] == "Spain" and competition['name'] == "Primera Division":
            return competition['code'], competition['id']

def get_matchday_matches(competition_id):
    response = requests.get('https://api.football-data.org/v2/competitions/' + str(competition_id) + '/matches', headers=HEADER)
    parsed_response = json.loads(response.text)
    for match in parsed_response['matches']:
        if match['matchday'] == match['season']['currentMatchday']:
            # if match['status'] == 'FINISHED': -> Commented so it can be tested before season starts
            new_match = Match(match['homeTeam']['name'], match['awayTeam']['name'], match['score']['fullTime']['homeTeam'], match['score']['fullTime']['awayTeam'])
            new_matches.append(new_match)


def main():
    competition_code, competition_id = get_competition_id()
    get_matchday_matches(competition_id)
    for match in new_matches:
        match.print_home_team()

if __name__ == '__main__':
    main()

    