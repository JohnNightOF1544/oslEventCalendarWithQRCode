from flask import Flask, render_template, redirect, request, session, url_for
from eventcalendar.app import app
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event import Event
from eventcalendar.models.department import Department
from eventcalendar.models.venue import Venue


@app.route('/student/event_info', methods=['GET', 'POST'])
def student_event_info():
	if "student_username" in session:
		student_username = session['student_username']
		if request.method == 'GET':



			test = Event.query.order_by(Event.id.desc()).all()
			


			eventInfoAccounts = Account.query.filter(Account.id.endswith('27')).all()
			eventInfoAccounttypes = AccountType.query.filter(AccountType.id.endswith('3')).all()
			eventInfoDepartments = Department.query.filter(Department.id.endswith('16')).all()

			return render_template('/student/student_template/eventInfo.html', test=test, eventInfoAccounts = eventInfoAccounts, eventInfoAccounttypes=eventInfoAccounttypes, eventInfoDepartments=eventInfoDepartments)
	
	else:
		return redirect(url_for('student_login'))




