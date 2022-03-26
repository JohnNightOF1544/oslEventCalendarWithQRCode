from flask import Flask, render_template, redirect, request, url_for, session, flash
from eventcalendar.app import app, db
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.department import Department
import bcrypt

@app.route('/admin/accounts', methods=['POST', 'GET'])
def admin_account():
	if "username" in session:
		username = session['username']

		if request.method == 'GET':			
			accounts = Account.query.filter_by(status="active").all()
			accountAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			accountDepartments = Department.query.all()
			accountAcctypes = AccountType.query.all()
			
			accountPage = ["/admin/osl_template/osl_account.html", '/admin/osl_modal/osl_modal_account.html']
			return render_template(accountPage, accounts=accounts, accountAcctypes=accountAcctypes, username=username, accountAccounttypes=accountAccounttypes, accountDepartments=accountDepartments)

		check_username = request.form['accountUsername']

		account_username = Account.query.filter_by(username= check_username).first()
	
		if account_username:
			return render_template('/log_register/username_taken.html' )



		if request.method == 'POST':
			account_name = request.form['accountFirst']
			account_middle = request.form['accountMiddle']
			account_last = request.form['accountLast']
			account_gender = request.form['accountGender']
			account_yearlevel = request.form['accountYearlevel']
			account_username = request.form['accountUsername']
			account_password = bcrypt.hashpw(request.form['accountPassword'].encode('UTF-8'), bcrypt.gensalt())
			account_type = AccountType.query.filter_by(name = "guest").first()
			department = Department.query.get(request.form['account_department'])
			new_account = Account(Fname = account_name, Mname = account_middle, Lname = account_last, gender = account_gender, year_level = account_yearlevel, username = account_username, password = account_password)
			new_account.department = department
			new_account.account_type = account_type

			db.session.add(new_account)
			db.session.commit()
			flash('Successfully Created')
			return redirect('/admin/accounts')

	return redirect(url_for('admin_login'))

@app.route('/admin/accounts/<int:id>', methods = ['UPDATE','GET'])
def manage_admin_account(id):
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			account = Account.query.get_or_404(id)
			if account:
				return {"id": account.id, "Fname": account.Fname, "Mname": account.Mname, "Lname": account.Lname, "gender": account.gender, "year_level": account.year_level, "username": account.username, "status": account.status, "department_id": account.department_id, "account_type_id": account.account_type_id}

			return {'message': 'Account type not found'}

		if request.method == 'UPDATE':
			updateAccount = Account.query.get_or_404(id)

			updateAccount.Fname = request.form['Fname']
			updateAccount.Mname = request.form['Mname']
			updateAccount.Lname = request.form['Lname']
			updateAccount.gender = request.form['gender']
			updateAccount.year_level = request.form['year_level']
			updateAccount.username = request.form['username']
			updateAccount.status = request.form['status']
			updateAccount.department_id = request.form['department_id']
			updateAccount.account_type_id = request.form['account_type_id']
			db.session.commit()
			return dict(id = id, Fname = updateAccount.Fname, Mname = updateAccount.Mname, Lname = updateAccount.Lname, gender = updateAccount.gender, year_level = updateAccount.year_level, username = updateAccount.username, status = updateAccount.status, department_id = updateAccount.department.name, account_type_id = updateAccount.account_type.name),200

		return {'message': 'There are a problem updating it'}
	
	return redirect(url_for('admin_login'))	