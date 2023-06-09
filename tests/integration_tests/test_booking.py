from app.models import models


class TestBookingRoute:

    request_form = {
        "club": "Iron Temple",
        "competition": "Fall Classic",
        "places": "3"
    }
    redirect_message = b"You should be redirected automatically to the target URL:"
    initial_points = b"Points available: 4"
    initial_places = b"Number of Places: 13"

    def test_route_failed_with_method_not_allowed(self, client, mocker, clubs_db_test, competitions_db_test):
        """
        GIVEN a valid club and competition names with correct number of requested_places
        WHEN the '/booking' page is requested (GET)
        THEN checks the response is valid, and a '405' status code is returned
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.get('/booking', data=self.request_form)
        assert response.status_code == 405
        assert b"The method is not allowed for the requested URL." in response.data

    def test_route_failed_with_wrong_club_name(self, client, mocker, clubs_db_test, competitions_db_test):
        """
        GIVEN a wrong club name and a valid competition name with correct number of requested_places
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid, and a '400' status code is returned with error message
        """
        request_form = {
            "club": "WRONG club name",
            "competition": "Fall Classic",
            "places": "3"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert self.redirect_message in response.data

    def test_route_failed_with_wrong_competition_name(self, client, mocker, clubs_db_test, competitions_db_test):
        """
        GIVEN a valid club name and a wrong competition name with correct number of requested_places
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "Iron Temple",
            "competition": "WRONG competition name",
            "places": "3"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert self.redirect_message in response.data

    def test_route_failed_with_no_number_of_requested_places(
            self, client, mocker, clubs_db_test, competitions_db_test
            ):
        """
        GIVEN valid club and competition names with no number of requested_places
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "Iron Temple",
            "competition": "Fall Classic",
            "places": ""
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"Please, enter a number." in response.data
        assert self.initial_points in response.data
        assert self.initial_places in response.data

    def test_route_failed_with_negative_number_of_requested_places(
            self, client, mocker, clubs_db_test, competitions_db_test
            ):
        """
        GIVEN valid club and competition names with negative number of requested_places
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "Iron Temple",
            "competition": "Fall Classic",
            "places": "-5"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"Please, enter a positive number." in response.data
        assert self.initial_points in response.data
        assert self.initial_places in response.data

    def test_route_failed_with_not_enough_club_points(self, client, mocker, clubs_db_test, competitions_db_test):
        """
        GIVEN valid club and competition names with number of requested_places greater than club points
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "Iron Temple",
            "competition": "Fall Classic",
            "places": "5"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"You have not enough points." in response.data
        assert self.initial_points in response.data
        assert self.initial_places in response.data

    def test_route_failed_with_not_enough_competition_places(
            self, client, mocker, clubs_db_test, competitions_db_test
            ):
        """
        GIVEN valid club and competition names with number of requested_places greater than competition places
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "TEST club with 20 points",
            "competition": "Competition with less than 12 places",
            "places": "12"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"There are not enough places for the competition." in response.data
        assert b"Points available: 20" in response.data
        assert b"Number of Places: 13" in response.data

    def test_route_failed_with_more_than_12_requested_places(
            self, client, mocker, clubs_db_test, competitions_db_test
            ):
        """
        GIVEN valid club and competition names with number of requested_places greater than 12
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "TEST club with 20 points",
            "competition": "Spring Festival",
            "places": "13"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"You cannot reserve more than 12 places per competition." in response.data
        assert b"Points available: 20" in response.data
        assert b"Number of Places: 25" in response.data

    def test_route_failed_with_past_competition(self, client, mocker, clubs_db_test, competitions_db_test):
        """
        GIVEN valid club and competition names with valid number of requested_places and past competition date
        WHEN the '/booking' page is posted to (POST)
        THEN checks the response is valid and a '400' status code is returned with error message
        """
        request_form = {
            "club": "She Lifts",
            "competition": "PAST Competition",
            "places": "5"
        }
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch.object(models, 'competitions', competitions_db_test)
        response = client.post('/booking', data=request_form)
        assert response.status_code == 400
        assert b"You cannot reserve places for past competitions." in response.data
        assert b"Points available: 12" in response.data
        assert b"Number of Places: 10" in response.data

    def test_route_success(self, client, mocker, test_club, test_competition):
        """
        GIVEN valid club and competition names with valid number of requested_places
        WHEN the '/booking' page is posted to (POST)
        THEN checks that response is valid and booking is complete
        """
        response = client.post('/booking', data=self.request_form)
        mocker.patch('app.models.models.get_club_by_name', return_value=test_club)
        mocker.patch('app.models.models.get_competition_by_name', return_value=test_competition)
        assert response.status_code == 200
        assert b"Great-booking complete for 3 places!" in response.data
        assert b"Points available: 1" in response.data
        assert b"Number of Places: 10" in response.data
