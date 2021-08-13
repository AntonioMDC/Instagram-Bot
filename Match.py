

from PIL.Image import new


class Match:
    already_uploaded = False

    def __init__(self,home_team, away_team, home_team_score, away_team_score, match_status):
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score
        self.match_status = match_status

    def change_home_team_score(self, new_score):
        self.home_team_score = new_score

    def change_away_team_score(self, new_score):
        self.away_team_score = new_score

    def print_home_team(self):
        print(self.home_team)

    def print_away_team(self):
        print(self.away_team)

    def get_status(self):
        return self.match_status