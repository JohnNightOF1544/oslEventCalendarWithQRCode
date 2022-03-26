from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event import Event
from eventcalendar.models.department import Department


@app.route('/student/events/', methods=['GET', 'POST'])
def student_event():
	if "student_username" in session:
		student_username = session['student_username']
		if request.method == 'GET':
			studentAccounttypes = AccountType.query.filter(AccountType.id.endswith('3')).all()
			studentDepartments = Department.query.filter(Department.id.endswith('16')).all()
			return render_template('/student/student_template/studentDash.html', student_username = student_username, studentAccounttypes=studentAccounttypes, studentDepartments=studentDepartments)
	else:
		return redirect(url_for('student_login'))

@app.route('/student/list_events/', methods = ['GET'])
def manage_studentEvents():
	if "student_username" in session:
		student_username = session['student_username']
		if request.method == 'GET':
			events = [dict(id = event.id, title = event.name, start= event.datetime_start, end = event.datetime_end,) for event in Event.query.all()]
			print(events)
			return dict(events = events)
	else:
		return redirect(url_for('student_login'))