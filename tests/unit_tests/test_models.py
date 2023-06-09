from app.models import models


class TestClubs:

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

    def test_load_clubs_should_return_none_with_FileNotFoundError(self, mocker):
        """
        GIVEN a mock for wrong path to clubs.json file
        WHEN the json.load fails
        THEN checks the return is none
        """
        mocker.patch.object(models, 'CLUBS_DATA', 'NOFILE.json')
        assert models.load_clubs() is None

    def test_get_club_by_email_should_return_logged_club(self, login_email, clubs_db_test, test_club):
        """
        GIVEN a existing user email and clubs list
        WHEN user logs in
        THEN returns club's data
        """
        assert models.get_club_by_email(login_email, clubs_db_test) == test_club

    def test_get_club_by_email_should_return_none_with_IndexError(self, clubs_db_test):
        """
        GIVEN clubs list and wrong user email
        WHEN user logs in
        THEN returns none
        """
        assert models.get_club_by_email("TEST@TEST.com", clubs_db_test) is None

    def test_get_club_by_email_should_return_none_with_no_value(self, clubs_db_test):
        """
        GIVEN clubs list and empty user email
        WHEN user logs in
        THEN returns none
        """
        assert models.get_club_by_email("", clubs_db_test) is None

    def test_get_club_by_name_should_return_club(self, mocker, clubs_db_test, test_club):
        """
        GIVEN a existing club name
        WHEN user is trying to book places
        THEN returns club's data
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        assert models.get_club_by_name("Iron Temple") == test_club

    def test_get_club_by_name_should_return_none_with_IndexError(self, mocker, clubs_db_test):
        """
        GIVEN a wrong club name
        WHEN user is trying to book places
        THEN returns none
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        assert models.get_club_by_name("TEST") is None

    def test_get_club_points_dict_should_return_club_points_list_of_dicts(self, mocker, clubs_db_test):
        """
        GIVEN list of clubs dict
        WHEN user access to index.html page
        THEN checks the return is the list of points by club
        """
        expected_value = [
            {'name': 'Simply Lift', 'points': '13'},
            {'name': 'Iron Temple', 'points': '4'},
            {'name': 'She Lifts', 'points': '12'},
            {'name': 'TEST club with 20 points', 'points': '20'}
        ]
        mocker.patch.object(models, 'clubs', clubs_db_test)
        assert models.get_club_points_dict(clubs_db_test) == expected_value

    def test_get_club_points_dict_should_return_none_with_Exception(self, mocker, clubs_db_test):
        """
        GIVEN list of clubs dict
        WHEN user access to index.html page
        THEN checks the return is None
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        assert models.get_club_points_dict(
            [{
                "ERRORname": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            }]
        ) is None


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

    def test_load_competitions_should_return_none_with_FileNotFoundError(self, mocker):
        """
        GIVEN a mock for wrong path to competitions.json file
        WHEN the json.load fails
        THEN checks the return is none
        """
        mocker.patch.object(models, 'COMPETITIONS_DATA', 'NOFILE.json')
        assert models.load_competitions() is None

    def test_get_competition_by_name_should_return_competition(self, mocker, competitions_db_test, test_competition):
        """
        GIVEN a existing competition name
        WHEN user is trying to book places
        THEN returns competition's data
        """
        mocker.patch.object(models, 'competitions', competitions_db_test)
        assert models.get_competition_by_name("Fall Classic") == test_competition


    def test_get_competition_by_name_should_return_none_with_IndexError(self, mocker, competitions_db_test):
        """
        GIVEN a wrong competition name
        WHEN user is trying to book places
        THEN returns none
        """
        mocker.patch.object(models, 'competitions', competitions_db_test)
        assert models.get_competition_by_name("TEST") is None
