from app.models import models
from app import server


class TestIndexRoute:

    ask_email = b"Please enter your secretary email to continue:"
    button = b"Enter"

    def test_route_success(self, client, mocker, clubs_db_test):
        """
        GIVEN a mock for clubs
        WHEN the '/' page is requested (GET)
        THEN checks the response is valid and data are displayed
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        response = client.get("/")
        assert response.status_code == 200
        assert self.ask_email in response.data
        assert self.button in response.data
        assert b"Simply Lift" in response.data
        assert b"Iron Temple" in response.data

    def test_route_failed_with_method_not_allowed(self, client, mocker, clubs_db_test):
        """
        GIVEN a mock for clubs
        WHEN the '/' page is posted to (POST)
        THEN checks the response is valid and a '405' status code is returned
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        response = client.post("/")
        assert response.status_code == 405
        assert self.ask_email not in response.data
        assert self.button not in response.data
        assert b"Simply Lift" not in response.data

    def test_route_failed_with_invalid_data_file(self, client, mocker):
        """
        GIVEN a wrong mock for club data file
        WHEN the '/' page is requested (GET)
        THEN checks the response is valid, and a '500' status code is returned with error message
        """
        mocker.patch.object(server, 'clubs', None)
        response = client.get("/")
        assert response.status_code == 500
        assert self.ask_email in response.data
        assert self.button in response.data
        assert b"500 Internal server error." in response.data
        assert b"Simply Lift" not in response.data

    def test_route_half_successful_with_club_points_list_none(self, client, mocker, clubs_db_test):
        """
        GIVEN a mock for clubs
        WHEN the '/' page is requested (GET)
        THEN checks the response is valid, and a '206' status code is returned with error message
        """
        mocker.patch.object(models, 'clubs', clubs_db_test)
        mocker.patch('app.models.models.get_club_points_dict', return_value=None)
        response = client.get("/")
        assert response.status_code == 206
        assert self.ask_email in response.data
        assert self.button in response.data
        assert b"Sorry, something went wrong with the display of club_points." in response.data
        assert b"Simply Lift" not in response.data
