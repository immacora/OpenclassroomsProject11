from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import models

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
    Route used for login with email to Flask application configured for testing.
    parameters:
        clubs: list
        competitions: list
    responses:
        500: none clubs or competitions, return index.
        400: email not found, return index.html.
        200: user is logged in, return welcome.html.
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
    return render_template('index.html'), 400


@routes.route('/show_booking/<competition>/<club>', methods=['GET'])
def show_booking(competition, club):
    club_found = models.get_club_by_name(club)
    competition_found = models.get_competition_by_name(competition)
    if club_found and competition_found:
        return render_template('booking.html', club=club_found, competition=competition_found)
    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=models.competitions)


@routes.route('/booking', methods=['POST'])
def booking():
    club_found = models.get_club_by_name(request.form['club'])
    competition_found = models.get_competition_by_name(request.form['competition'])
    placesRequired = int(request.form['places'])
    competition_found['number_of_places'] = int(competition_found['number_of_places'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club_found, competitions=models.competitions)


# TODO: Add route for points display


@routes.route('/logout')
def logout():
    return redirect(url_for('routes.index'))
