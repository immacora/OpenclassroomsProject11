from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import models
from .helpers import calculate_remaining_points_and_places, check_competition_date

routes = Blueprint('routes', __name__)
clubs = models.clubs
competitions = models.competitions


@routes.route('/', methods=['GET'])
def index():
    """Entry point to Flask application displaying login form."""
    return render_template('index.html')


@routes.route('/show_summary', methods=['POST'])
def show_summary():
    """
    Show summary route, need to login with email.
    global variables:
        clubs: list
        competitions: list
    responses:
        200: club email found, return welcome.html.
        500: none clubs or competitions, return index.html
        404: club email not found, return index.html.
    """
    if not clubs or not competitions:
        flash("500 Internal server error. \
              Sorry, something went wrong. \
              Please try again later and contact us if it persists.")
        return render_template('index.html'), 500

    logged_club = models.get_club_by_email(request.form['email'], clubs)
    if logged_club:
        return render_template('welcome.html', club=logged_club, competitions=competitions)

    flash("Sorry, that email was not found.")
    return render_template('index.html'), 404


@routes.route('/show_booking/<competition>/<club>', methods=['GET'])
def show_booking(competition, club):
    """
    Shows club name and available points, available competition places, and number of places booking form.
    parameters:
        club name: str
        competition name: str
    responses:
        200: club and competition found, return booking.html.
        404: club or competition not found, return index.html.
    """
    club_found = models.get_club_by_name(club)
    competition_found = models.get_competition_by_name(competition)

    if club_found and competition_found:
        return render_template('booking.html', club=club_found, competition=competition_found)

    flash("The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
    return redirect(url_for('routes.index')), 404


@routes.route('/booking', methods=['POST'])
def booking():
    """
    Books the number of competition places for the club and the competition filled in the form.
    responses:
        200: club and competition found with correct number of requested_places, return welcome.html.
        400: bad request for number of requested_places and past competition, return welcome.html.
        400: no club or competition matches data request.form, return index.html.
    """
    club_found = models.get_club_by_name(request.form['club'])
    competition_found = models.get_competition_by_name(request.form['competition'])

    if club_found and competition_found:
        current_competition = check_competition_date(competition_found['date'])

        if not isinstance(current_competition, str):
            remaining_points_and_places = calculate_remaining_points_and_places(request.form['places'], club_found['points'], competition_found['number_of_places'])

            if not isinstance(remaining_points_and_places, str):
                club_found['points'] = remaining_points_and_places.get("remaining_club_points")
                competition_found['number_of_places'] = remaining_points_and_places.get("remaining_competition_places")
                requested_places = remaining_points_and_places.get("requested_places")
                flash(f"Great-booking complete for {requested_places} places!")
                return render_template('welcome.html', club=club_found, competitions=competitions)
            else:
                flash(remaining_points_and_places)
        else:
            flash(current_competition)

        return render_template('welcome.html', club=club_found, competitions=competitions), 400

    flash("Something went wrong. Please try again or contact us if it persists.")
    return redirect(url_for('routes.index')), 400


# TODO: Add route for points display


@routes.route('/logout')
def logout():
    return redirect(url_for('routes.index'))
