from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event_type import EventType

from eventcalendar.models.request_form import RequestForm

@app.route('/admin/request_events', methods=['POST', 'GET'])
def request_event():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			requestEvents = RequestForm.query.order_by(RequestForm.id.desc()).all()
			requestEventtypes = EventType.query.order_by(EventType.id).all()
			requestAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_event_request.html', requestEvents=requestEvents, requestEventtypes=requestEventtypes, requestAccounttypes=requestAccounttypes, username=username)
	else:
		return redirect(url_for('admin_login'))


@app.route('/admin/request_events/<int:id>', methods = ['DELETE'])
def manage_request_events(id):
	if "username" in session:
		username = session['username']
		if request.method == 'DELETE':
			deleteRequest = RequestForm.query.get_or_404(id)
			try:
				db.session.delete(deleteRequest)
				db.session.commit()
				return {"message": "Event successfully deleted"},200
			except:
				return 'There are a problem deleting'
	else:
		return redirect(url_for('admin_login'))