from app.models import models


class TestClubs:

    clubs = [
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
        }
    ]

    test_club = {
            "name":"Iron Temple",
            "email": "admin@irontemple.com",
            "points":"4"
    }

    def test_load_clubs_should_return_clubs(self):
        """
        GIVEN a path constant CLUBS_DATA to clubs.json file
        WHEN clubs are loaded
        THEN checks clubs names exists in the returned list
        """
        expected_value_1 = "Simply Lift"
        expected_value_2 = "Iron Temple"
        expected_value_3 = "She Lifts"
        rv = str(models.load_clubs())
        assert expected_value_1 in rv
        assert expected_value_2 in rv
        assert expected_value_3 in rv

    def test_load_clubs_should_return_none_whith_FileNotFoundError(self, mocker):
        """
        GIVEN a mock for wrong path to clubs.json file
        WHEN the json.load fails
        THEN checks the return is none
        """
        mocker.patch.object(models, 'CLUBS_DATA', 'NOFILE.json')
        assert models.load_clubs() is None

    def test_get_club_by_email_should_return_logged_club(self):
        """
        GIVEN a existing user email and clubs list
        WHEN user logs in
        THEN returns club's data
        """
        assert models.get_club_by_email("admin@irontemple.com", self.clubs) == self.test_club

    def test_get_club_by_email_should_return_none_whith_IndexError(self):
        """
        GIVEN clubs list and wrong user email
        WHEN user logs in
        THEN returns none
        """
        assert models.get_club_by_email("TEST@TEST.com", self.clubs) is None

    def test_get_club_by_email_should_return_none_whith_no_value(self):
        """
        GIVEN clubs list and empty user email
        WHEN user logs in
        THEN returns none
        """
        assert models.get_club_by_email("", self.clubs) is None


class TestCompetitions:

    def test_load_competitions_should_return_competitions(self):
        """
        GIVEN a path constant COMPETITIONS_DATA to competitions.json file
        WHEN competitions are loaded
        THEN checks competitions names exists in the returned list
        """
        expected_value_1 = "Spring Festival"
        expected_value_2 = "Fall Classic"
        rv = str(models.load_competitions())
        assert expected_value_1 in rv
        assert expected_value_2 in rv

    def test_load_competitions_should_return_none_whith_FileNotFoundError(self, mocker):
        """
        GIVEN a mock for wrong path to competitions.json file
        WHEN the json.load fails
        THEN checks the return is none
        """
        mocker.patch.object(models, 'COMPETITIONS_DATA', 'NOFILE.json')
        assert models.load_competitions() is None
