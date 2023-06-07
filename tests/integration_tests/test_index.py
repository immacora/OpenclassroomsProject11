class TestIndexRoute:

    ask_email = b"Please enter your secretary email to continue:"
    button = b"Enter"

    def test_route_success(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN checks the response is valid
        """
        response = client.get("/")
        assert response.status_code == 200
        assert self.ask_email in response.data
        assert self.button in response.data


    def test_route_failed(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is posted to (POST)
        THEN checks the response is valid and a '405' status code is returned
        """
        response = client.post("/")
        assert response.status_code == 405
        assert self.ask_email not in response.data
        assert self.button not in response.data
