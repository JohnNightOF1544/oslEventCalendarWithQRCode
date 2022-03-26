from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event import Event

@app.route('/admin/events', methods=['POST', 'GET'])
def admin_event():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			eventAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_event.html', username=username, eventAccounttypes=eventAccounttypes)
	else:
		
		return redirect(url_for('admin_login'))


@app.route('/admin/list_events/', methods = ['GET'])
def manage_events():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			events = [dict(id = event.id, title = event.name, start= event.datetime_start, end = event.datetime_end) for event in Event.query.all()]
			# print(events)
			return dict(events = events, username=username)
	else:
		
		return redirect(url_for('admin_login'))