from app import server


class TestAuthentication:

    def test_login_route_success(self, client):
        """
        GIVEN a existing user email for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks that response is valid, user is logged in and data are displayed
        """
        response = client.post('/show_summary', data={"email": "admin@irontemple.com"})
        assert response.status_code == 200
        assert b"Welcome, admin@irontemple.com" in response.data
        assert b'Competitions:' in response.data
        assert b'Logout' in response.data

    def test_login_route_failed_whith_invalid_login(self, client):
        """
        GIVEN a wrong user email for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks that response is valid, '400' status code is returned and error message is displayed
        """
        response = client.post('/show_summary', data={"email": "wrong_email@test.com"})
        assert response.status_code == 400
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data
        assert b"Sorry, that email was not found." in response.data

    def test_login_route_failed_whith_invalid_data_file(self, client, mocker):
        """
        GIVEN a existing user email whith a wrong mock for data file for login to Flask application configured for testing
        WHEN the '/show_summary' page is posted to (POST)
        THEN checks the response is valid, '500' status code is returned and error message is displayed
        """
        mocker.patch.object(server, 'clubs', None)
        mocker.patch.object(server, 'competitions', None)
        response = client.post('/show_summary', data={"email": "admin@irontemple.com"})
        assert response.status_code == 500
        assert b"Welcome, admin@irontemple.com" not in response.data
        assert b"Please enter your secretary email to continue:" in response.data
        assert b"500 Internal server error." in response.data

    def test_logout_route(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/logout' page is requested (GET)
        THEN checks the response is valid and the user is redirect to the 'index' page
        """
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert b"Please enter your secretary email to continue:" in response.data
        assert b'Logout' not in response.data
