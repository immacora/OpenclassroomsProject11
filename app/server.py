from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import models

routes = Blueprint('routes', __name__)
clubs = models.load_clubs()
competitions = models.load_competitions()


@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/show_summary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


@routes.route('/book/<competition>/<club>')
def show_booking(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@routes.route('/booking',methods=['POST'])
def booking():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['number_of_places'] = int(competition['number_of_places'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@routes.route('/logout')
def logout():
    return redirect(url_for('routes.index'))
