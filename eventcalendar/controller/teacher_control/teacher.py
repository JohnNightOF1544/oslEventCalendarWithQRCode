from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app
from eventcalendar.models.event import Event
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.department import Department


@app.route('/teacher/events', methods=['GET', 'POST'])
def teacher_event():
	if "teacher_username" in session:
		teacher_username = session['teacher_username']
		if request.method == 'GET':
			teacherAccounttypes = AccountType.query.filter(AccountType.id.endswith('2')).all()
			teacherDepartments = Department.query.filter(Department.id.endswith('16')).all()
			return render_template('/teacher/teacher_template/TeacherDash.html', teacher_username=teacher_username, teacherAccounttypes=teacherAccounttypes, teacherDepartments=teacherDepartments)
	else:
		return redirect(url_for('teacher_login'))

@app.route('/teacher/list_events/', methods = ['GET'])
def manage_teacherEvents():
	if "teacher_username" in session:
		if request.method == 'GET':
			events = [dict(id = event.id, title = event.name, start= event.datetime_start, end = event.datetime_end,) for event in Event.query.all()]
			print(events)
			return dict(events = events)
	else:
		return redirect(url_for('teacher_login'))