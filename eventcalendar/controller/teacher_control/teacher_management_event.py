from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.event import Event
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.department import Department
from eventcalendar.models.request_form import RequestForm



@app.route('/teacher/manage_events', methods=['GET', 'POST'])
def teacher_manage_event():
	if "teacher_username" in session:
		teacher_username = session['teacher_username']
		if request.method == 'GET':
			teacherManageevents = Event.query.order_by(Event.id.desc()).all()
			teacherManageaccounttypes = AccountType.query.filter(AccountType.id.endswith('2')).all()
			teachermanagedepartments = Department.query.filter(Department.id.endswith('16')).all()
			teacherRequestdepartments = Department.query.all()
			return render_template('/teacher/teacher_template/teacher_requestEvent.html', teacher_username=teacher_username, teacherManageaccounttypes=teacherManageaccounttypes, teachermanagedepartments=teachermanagedepartments, teacherManageevents=teacherManageevents, teacherRequestdepartments=teacherRequestdepartments)

		if request.method == 'POST':
			teacherReaquestevent = request.form['requestEvents']
			requeststart = request.form['requestStart']
			requestend = request.form['requestEnd']
			teacherRequestdescription = request.form['requestDescription']
			department = Department.query.get(request.form['request_department'])
			new_request = RequestForm(name = teacherReaquestevent, description=teacherRequestdescription, datetime_start=requeststart, datetime_end=requestend)
			new_request.department = department
			db.session.add(new_request)
			db.session.commit()
			return redirect('/requested/list')
	else:
		return redirect(url_for('teacher_login'))