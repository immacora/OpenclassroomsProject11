from app import server


class TestShowBookingRoute:

    def test_route_success(self, client, mocker, test_club, test_competition):
        """
        GIVEN a mock for club and competition names
        WHEN the '/show_booking' page is requested (GET)
        THEN checks the response is valid, and data are displayed
        """
        mocker.patch('app.models.models.get_club_by_name', return_value=test_club)
        mocker.patch('app.models.models.get_competition_by_name', return_value=test_competition)
        response = client.get('/show_booking/Fall Classic/Iron Temple')
        assert response.status_code == 200
        assert b"Fall Classic" in response.data
        assert b"Points available: 4" in response.data
        assert b"Places available: 13" in response.data
        assert b"How many places?" in response.data
        assert b"Book" in response.data

    def test_route_failed_with_method_not_allowed(self, client, mocker, test_club, test_competition):
        """
        GIVEN a mock for club and competition names
        WHEN the '/show_booking' page is posted to (POST)
        THEN checks the response is valid, and a '405' status code is returned
        """
        mocker.patch('app.models.models.get_club_by_name', return_value=test_club)
        mocker.patch('app.models.models.get_competition_by_name', return_value=test_competition)
        response = client.post('/show_booking/Fall Classic/Iron Temple')
        assert response.status_code == 405
        assert b"The method is not allowed for the requested URL." in response.data

    def test_route_failed_with_wrong_club_name(self, client, mocker, clubs_db_test, test_competition):
        """
        GIVEN a wrong club name and a mock for competition name
        WHEN the '/show_booking' page is requested (GET)
        THEN checks the response is valid, and a '404' status code is returned with error message
        """
        mocker.patch.object(server, 'clubs', clubs_db_test)
        mocker.patch('app.models.models.get_competition_by_name', return_value=test_competition)
        response = client.get('/show_booking/Fall Classic/WRONG club name', follow_redirects=True)
        assert response.status_code == 404
        assert b"You should be redirected automatically to the target URL:" in response.data

    def test_route_failed_with_wrong_competition_name(self, client, mocker, competitions_db_test, test_club):
        """
        GIVEN a mock for club name and a wrong competition name
        WHEN the '/show_booking' page is requested (GET)
        THEN checks the response is valid, and a '404' status code is returned with error message
        """
        mocker.patch.object(server, 'competitions', competitions_db_test)
        mocker.patch('app.models.models.get_club_by_name', return_value=test_club)
        response = client.get('/show_booking/WRONG competition name/Iron Temple', follow_redirects=True)
        assert response.status_code == 404
        assert b"You should be redirected automatically to the target URL:" in response.data
