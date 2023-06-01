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
