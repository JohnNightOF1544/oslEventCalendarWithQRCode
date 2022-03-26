from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event_type import EventType
from eventcalendar.models.department import Department
from eventcalendar.models.event import Event
from eventcalendar.models.venue import Venue
from eventcalendar.models.request_form import RequestForm

@app.route('/admin/manage_events', methods=['POST', 'GET'])
def manage_admin_event():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			manageDepartments = Department.query.order_by(Department.id).all()
			manageEvents = Event.query.order_by(Event.id.desc()).all()
			manageRequestevents = RequestForm.query.order_by(RequestForm.id.desc()).all()
			manageEventtypes = EventType.query.order_by(EventType.id).all()
			manageVenues = Venue.query.order_by(Venue.id).all()
			eventAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_manage_events.html', manageRequestevents=manageRequestevents,manageEvents=manageEvents, manageEventtypes=manageEventtypes, manageVenues=manageVenues, manageDepartments=manageDepartments, username=username, eventAccounttypes=eventAccounttypes)

		if request.method == 'POST':
			eventname = request.form['eventName']
			eventstart = request.form['eventStart']
			eventend = request.form['eventEnd']
			eventstatus = request.form['eventStatus']
			event_type = EventType.query.get(request.form['manageEventtype'])
			venue = Venue.query.get(request.form['manageVenue'])
			department = Department.query.get(request.form['manageDepartment'])
			new_event = Event(name = eventname, datetime_start = eventstart, datetime_end = eventend, status = eventstatus)
			new_event.event_type = event_type
			new_event.venue = venue
			new_event.department = department
			db.session.add(new_event)
			db.session.commit()
			return redirect('/admin/manage_events')
	else:
		
		return redirect(url_for('admin_login'))


@app.route('/admin/manage_events/<int:id>', methods = ['DELETE'])
def manage_admin_events(id):
	if "username" in session:
		username = session['username']

		if request.method == 'DELETE':
			deleteEvent = Event.query.get_or_404(id)
			try:
				db.session.delete(deleteEvent)
				db.session.commit()
				return {"message": "Event successfully deleted"},200
			except:
				return 'There are a problem deleting'
	else:
		
		return redirect(url_for('admin_login'))