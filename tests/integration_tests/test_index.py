def test_index_route_success(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN checks the response is valid
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Please enter your secretary email to continue:" in response.data


def test_index_route_failed(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN checks the response is valid and a '405' status code is returned
    """
    response = client.post("/")
    assert response.status_code == 405
    assert b"Please enter your secretary email to continue:" not in response.data
