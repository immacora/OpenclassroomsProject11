import pytest
from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    yield app.test_client()


@pytest.fixture
def clubs_db_test():
    return [
        {
            "name":"Simply Lift",
            "email":"john@simplylift.co",
            "points":"13"
        },
        {
            "name":"Iron Temple",
            "email": "admin@irontemple.com",
            "points":"4"
        },
        {   "name":"She Lifts",
            "email": "kate@shelifts.co.uk",
            "points":"12"
        },
        {   "name":"TEST club with 20 points",
            "email": "TESTclub with 20 points@20 points.com",
            "points":"20"
        }
    ]


@pytest.fixture
def competitions_db_test():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "number_of_places": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "number_of_places": "13"
        }
    ]


@pytest.fixture
def test_club():
    return {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    }


@pytest.fixture
def test_competition():
    return {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "number_of_places": "13"
    }


@pytest.fixture
def login_email():
    return "admin@irontemple.com"
