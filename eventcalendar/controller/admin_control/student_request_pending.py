from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event_type import EventType
from eventcalendar.models.department import Department

@app.route('/admin/pending_request', methods=['POST', 'GET'])
def pending_request():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			pendingAccounts = Account.query.filter_by(account_type_id="4").all()
			pendingEventtypes = EventType.query.order_by(EventType.id).all()
			pendingAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			pendindDeparments = Department.query.all()
			pendingaccountTypes = AccountType.query.all()
			return render_template('/admin/osl_template/student_pending_request.html', username=username, pendingAccounts=pendingAccounts, pendingEventtypes=pendingEventtypes, pendingAccounttypes=pendingAccounttypes, pendindDeparments=pendindDeparments, pendingaccountTypes=pendingaccountTypes)
	else:
		return redirect(url_for('admin_login'))

@app.route('/admin/pending_request/<int:id>', methods = ['UPDATE','GET'])
def manage_pending_request(id):
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			account = Account.query.get_or_404(id)
			if account:
				return {"id": account.id, "Fname": account.Fname, "Mname": account.Mname, "Lname": account.Lname, "gender": account.gender, "year_level": account.year_level, "username": account.username, "status": account.status, "department_id": account.department_id, "account_type_id": account.account_type_id}
			else:
				return {'message': 'Account type not found'}

		if request.method == 'UPDATE':
			pendingAccount = Account.query.get_or_404(id)
			try:
				pendingAccount.Fname = request.form['Fname']
				pendingAccount.Mname = request.form['Mname']
				pendingAccount.Lname = request.form['Lname']
				pendingAccount.gender = request.form['gender']
				pendingAccount.year_level = request.form['year_level']
				pendingAccount.username = request.form['username']
				pendingAccount.status = request.form['status']
				pendingAccount.department_id = request.form['department_id']
				pendingAccount.account_type_id = request.form['account_type_id']
				db.session.commit()
				return dict(id = id, Fname = pendingAccount.Fname, Mname = pendingAccount.Mname, Lname = pendingAccount.Lname, gender = pendingAccount.gender, year_level = pendingAccount.year_level, username = pendingAccount.username, status = pendingAccount.status, department_id = pendingAccount.department.name, account_type_id = pendingAccount.account_type.name),200

			except:
				return 'There are a problem updating it'
	else:
		return redirect(url_for('admin_login'))	