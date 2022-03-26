from flask import Flask, render_template, request, redirect, url_for
from eventcalendar.app import app

from eventcalendar.models.department import Department
from eventcalendar.models.event import Event
from eventcalendar.models.event_participant import EventParticipant
from eventcalendar.models.event_type import EventType
from eventcalendar.models.venue import Venue

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		myKasadyaan = Event.query.limit(1).all()
		mySss = Venue.query.limit(1)
		myDepart = Department.query.limit(1).all()
		return render_template('/homePage/homePage.html', myKasadyaan=myKasadyaan, mySss=mySss, myDepart=myDepart)
		