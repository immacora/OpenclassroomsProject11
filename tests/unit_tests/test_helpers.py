from app import helpers


class TestGetPlusIntegerValue:
    """
    GIVEN a value from a user input
    WHEN the form is submitted
    THEN checks the return is a positive integer or an error message
    """
    error_message = "Please, enter a number."

    def test_should_return_integer(self):
        assert helpers.get_plus_integer_value("5") == 5

    def test_with_float_value_should_return_error_message(self):
        assert helpers.get_plus_integer_value("5.5") == self.error_message

    def test_with_no_number_should_return_error_message(self):
        assert helpers.get_plus_integer_value("a") == self.error_message

    def test_with_no_value_should_return_error_message(self):
        assert helpers.get_plus_integer_value("") == self.error_message

    def test_with_negative_value_should_return_error_message(self):
        assert helpers.get_plus_integer_value("-5") == "Please, enter a positive number."


class TestCalculateSubstraction:
    """
    GIVEN two numbers
    WHEN we want to do a subtraction
    THEN checks the return is a positive integer or None
    """
    requested_places = 4

    def test_should_return_positive_integer(self):
        assert helpers.calculate_substraction(4, self.requested_places) == 0

    def test_with_zero_number_should_return_none(self):
        assert helpers.calculate_substraction(0, self.requested_places) is None

    def test_with_negative_number_should_return_none(self):
        assert helpers.calculate_substraction(-2, self.requested_places) is None

    def test_with_fewer_number_than_number_to_subtract_should_return_none(self):
        assert helpers.calculate_substraction(2, self.requested_places) is None


class TestCalculateRemainingPointsAndPlaces:
    """
    GIVEN three str values
    WHEN user wants to books places
    THEN checks the return is a dict containing positive integers for requested_places, remaining_club_points, remaining_competition_places or an error message
    """
    club_points = "4"
    competition_places = "10"

    def test_should_return_dict(self):
        expected_value = {
            "requested_places": 4,
            "remaining_club_points": 0,
            "remaining_competition_places": 6
        }
        assert helpers.calculate_remaining_points_and_places("4", self.club_points, self.competition_places) == expected_value

    def test_with_negative_requested_places_should_return_error_message(self):
        assert helpers.calculate_remaining_points_and_places("-4", self.club_points, self.competition_places) == "Please, enter a positive number."

    def test_with_no_int_requested_places_should_return_error_message(self):
        assert helpers.calculate_remaining_points_and_places("!", self.club_points, self.competition_places) == "Please, enter a number."

    def test_with_higher_requested_places_than_club_points_should_return_error_message(self):
        assert helpers.calculate_remaining_points_and_places("5", self.club_points, self.competition_places) == "You have not enough points."

    def test_with_higher_requested_places_than_competition_places_should_return_error_message(self):
        assert helpers.calculate_remaining_points_and_places("11", "11", self.competition_places) == "There are not enough places for the competition."

    def test_with_requested_places_more_than_12_should_return_error_message(self):
        assert helpers.calculate_remaining_points_and_places("13", "20", "25") == "You cannot reserve more than 12 places per competition."
