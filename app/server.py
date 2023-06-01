from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import models

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/show_summary', methods=['POST'])
def show_summary():
    logged_club = models.get_club_by_email(request.form['email'])
    return render_template('welcome.html', club=logged_club, competitions=models.competitions)


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
