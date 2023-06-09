import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
CLUBS_DATA = BASE_DIR.joinpath('clubs.json')
COMPETITIONS_DATA = BASE_DIR.joinpath('competitions.json')


def load_clubs():
    """Returns list of the test application's clubs.json file."""
    try:
        with open(CLUBS_DATA) as c:
            clubs = json.load(c)['clubs']
            return clubs
    except FileNotFoundError as e:
        print("Failed to load clubs:", e)


def load_competitions():
    """Returns list of the test application's competitions.json file."""
    try:
        with open(COMPETITIONS_DATA) as comps:
            competitions = json.load(comps)['competitions']
            return competitions
    except FileNotFoundError as e:
        print("Failed to load competitions:", e)


clubs = load_clubs()
competitions = load_competitions()


def get_club_by_email(email, clubs):
    """Returns the club found by email."""
    try:
        return [club for club in clubs if club['email'] == email][0]
    except IndexError as e:
        print("Email not found:", e)


def get_club_by_name(club_name):
    """Returns the club found by name."""
    try:
        return [c for c in clubs if c['name'] == club_name][0]
    except IndexError as e:
        print("Club not found:", e)


def get_competition_by_name(competition_name):
    """Returns the competition found by name."""
    try:
        return [c for c in competitions if c['name'] == competition_name][0]
    except IndexError as e:
        print("Competition not found:", e)


def get_club_points_dict(clubs):
    """Returns the list of club points dict."""
    club_points = []
    try:
        for club in clubs:
            name = club["name"]
            points = club["points"]
            club = {
                "name": name,
                "points": points
            }
            club_points.append(club)
        return club_points
    except Exception as e:
        print("Failed to extract club points:", e)
