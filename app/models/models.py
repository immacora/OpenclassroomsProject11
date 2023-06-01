import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
CLUBS_DATA = BASE_DIR.joinpath('clubs.json')
COMPETITIONS_DATA = BASE_DIR.joinpath('competitions.json')


def load_clubs():
    with open(CLUBS_DATA) as c:
        clubs = json.load(c)['clubs']
        return clubs


def load_competitions():
    with open(COMPETITIONS_DATA) as comps:
        competitions = json.load(comps)['competitions']
        return competitions


clubs = load_clubs()
competitions = load_competitions()


def get_club_by_email(email):
    logged_club = [club for club in clubs if club['email'] == email][0]
    return logged_club


def get_club_by_name(club_name):
    club_found = [c for c in clubs if c['name'] == club_name][0]
    return club_found


def get_competition_by_name(competition_name):
    competition_found = [c for c in competitions if c['name'] == competition_name][0]
    return competition_found
