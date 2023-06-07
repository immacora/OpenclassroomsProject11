from app import server


class TestAuthentication:

    ask_email = b"Please enter your secretary email to continue:"
    logout_button = b"Logout"

    def test_login_route_success(self, mocker, client, clubs_db_test, login_email):
        """
        GIVEN a existing user email for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks that response is valid, user is logged in and data are displayed
        """
        mocker.patch.object(server, 'clubs', clubs_db_test)
        response = client.post('/show_summary', data={"email": login_email})
        assert response.status_code == 200
        assert f"Welcome, {login_email}" in response.data.decode()
        assert b'Competitions:' in response.data
        assert self.logout_button in response.data

    def test_login_route_failed_with_invalid_login(self, mocker, client, clubs_db_test):
        """
        GIVEN a wrong user email for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks that response is valid, '400' status code is returned and error message is displayed
        """
        mocker.patch.object(server, 'clubs', clubs_db_test)
        response = client.post('/show_summary', data={"email": "wrong_email@test.com"})
        assert response.status_code == 404
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data
        assert b"Sorry, that email was not found." in response.data

    def test_login_route_failed_with_invalid_data_file(self, client, mocker, login_email):
        """
        GIVEN a existing user email with a wrong mock for data file for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks the response is valid, '500' status code is returned and error message is displayed
        """
        mocker.patch.object(server, 'clubs', None)
        mocker.patch.object(server, 'competitions', None)
        response = client.post('/show_summary', data={"email": login_email})
        assert response.status_code == 500
        assert f"Welcome, {login_email}" not in response.data.decode()
        assert self.ask_email in response.data
        assert b"500 Internal server error." in response.data

    def test_logout_route(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/logout' page is requested (GET)
        THEN checks the response is valid and the user is redirected to the 'index' page
        """
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert self.ask_email in response.data
        assert self.logout_button not in response.data
