import requests
import json
from input import *
from Match import Match
import time
from InstagramBot import * 
from image_generator import * 


matchday_matches = []


def get_competition_id():
    response = requests.get('https://api.football-data.org/v2/competitions/', headers=HEADER)
    parsed_response = json.loads(response.text)
    for competition in parsed_response['competitions']:
        if competition['area']['name'] == "Spain" and competition['name'] == "Primera Division":
            return competition['code'], competition['id']


def get_matchday_matches(competition_id):
    response = requests.get('https://api.football-data.org/v2/competitions/' + str(competition_id) + '/matches', headers=HEADER)
    parsed_response = json.loads(response.text)

    matchday = parsed_response['matches'][0]['season']['currentMatchday']
    with open('data.txt', 'w') as outfile:
        json.dump(parsed_response, outfile)
        
    response_current_matchday_matches = requests.get('https://api.football-data.org/v2/competitions/' + str(competition_id) 
                                                    + '/matches?' + 'matchday=' + str(matchday), headers=HEADER)
    parsed_response_current_matchday_matches = json.loads(response_current_matchday_matches.text)
    
    for match in parsed_response_current_matchday_matches['matches']:
        new_match = Match(match['homeTeam']['name'], match['awayTeam']['name'], match['score']['fullTime']['homeTeam'], 
                            match['score']['fullTime']['awayTeam'], match['status'])
        matchday_matches.append(new_match)

    return matchday


def check_changes_and_upload_if_match_finished(competition_id, matchday, insta_bot):
    response = requests.get('https://api.football-data.org/v2/competitions/' + str(competition_id) 
                            + '/matches?' + str(matchday), headers=HEADER)
    parsed_response = json.loads(response.text)

    for new_match, match in zip(parsed_response['matches'], matchday_matches):
        if new_match['status'] == "FINISHED" and match.already_uploaded == False:
            match.change_home_team_score(new_match['score']['fullTime']['homeTeam'])
            match.change_away_team_score(new_match['score']['fullTime']['awayTeam'])

            print("Uploading ", match.home_team, " vs ", match.away_team, " photo...")

            create_and_upload_photo(insta_bot, match)

    return matchday


def create_and_upload_photo(insta_bot, match):
    photo_path = create_photo(match)
    insta_bot.login()
    insta_bot.upload_photo(photo_path)
    match.already_uploaded = True


def check_unfinished_matches():
    for match in matchday_matches:
        if match.already_uploaded == False:
            return True

    return False


def main():
    insta_bot = InstagramBot()
    competition_code, competition_id = get_competition_id()
    current_matchday = get_matchday_matches(competition_id)

    while check_unfinished_matches():
        check_changes(competition_id, current_matchday, insta_bot)
        time.sleep(7200)

    print("Matchday Finished")


if __name__ == "__main__":
    main()