from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.department import Department
from eventcalendar.models.request_form import RequestForm



@app.route('/requested/list', methods=['GET', 'POST'])
def teacher_requested_list():
	if "teacher_username" in session:
		teacher_username = session['teacher_username']
		if request.method == 'GET':
			teacherRequestlists = RequestForm.query.order_by(RequestForm.id.desc()).all()
			teacherRequestaccounttypes = AccountType.query.filter(AccountType.id.endswith('2')).all()
			teacherRequestfilterdepartments = Department.query.filter(Department.id.endswith('16')).all()
			teacherRequestdepartments = Department.query.all()
			return render_template('/teacher/teacher_template/teacherRequestpage.html', teacher_username=teacher_username, teacherRequestaccounttypes=teacherRequestaccounttypes, teacherRequestfilterdepartments=teacherRequestfilterdepartments, teacherRequestlists=teacherRequestlists, teacherRequestdepartments=teacherRequestdepartments)
	else:
		return redirect(url_for('teacher_login'))

@app.route('/requested/list/<int:id>', methods = ['DELETE'])
def manage_teacher_events(id):
	if "teacher_username" in session:
		if request.method == 'DELETE':
			deleteRequest = RequestForm.query.get_or_404(id)
			try:
				db.session.delete(deleteRequest)
				db.session.commit()
				return {"message": "Event successfully deleted"},200
			except:
				return 'There are a problem deleting'
	else:
		return redirect(url_for('teacher_login'))