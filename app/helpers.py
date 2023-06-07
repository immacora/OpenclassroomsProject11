def get_plus_integer_value(value):
    """Return positive number or error message."""
    try:
        int_value = int(value)
        return "Please, enter a positive number." if int_value < 0 else int_value
    except ValueError:
        return "Please, enter a number."


def calculate_substraction(number, number_to_subtract):
    """Return substraction result or None."""
    if number >= number_to_subtract and number >= 0:
        result = number - number_to_subtract
        return result
    else:
        return None


def calculate_remaining_points_and_places(requested_places, club_points, competition_places):
    """
    Checks if requested places is a positive integer less than or equal to club points and 12 max competition places and return calculated remaining points and places.
    Parameters:
        requested_places (str): The number to subtract from club points and competition places
        club_points (str): The number of club points available
        competition_places (str): The number of competition places available
    Returns:
        str: Error message.
        dict: requested_places, remaining_club_points, remaining_competition_places.
    """
    requested_places = get_plus_integer_value(requested_places)

    if not isinstance(requested_places, str):

        if requested_places > 12:
            return "You cannot reserve more than 12 places per competition."

        remaining_club_points = calculate_substraction(int(club_points), requested_places)
        remaining_competition_places = calculate_substraction(int(competition_places), requested_places)

        if remaining_club_points is None:
            return "You have not enough points."
        elif remaining_competition_places is None:
            return "There are not enough places for the competition."
        else:
            return {
                "requested_places": requested_places,
                "remaining_club_points": remaining_club_points,
                "remaining_competition_places": remaining_competition_places
            }

    return requested_places
