from flask import Flask, render_template, request, redirect, url_for, session, flash
from eventcalendar.app import app
import bcrypt
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType

@app.route('/adminlogout')
def adminlogout():
	session.clear()
	flash('The username or password invalid.')
	return redirect(url_for('admin_login'))

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
	if request.method == 'POST':
		session.permanent = True
		username = request.form['username']
		password = request.form['password']
		session["username"] = username

		account = Account.query.filter_by(username = username, status="active").first()
		if account:
			if bcrypt.checkpw(password.encode('UTF-8'), account.password.encode('UTF-8')):
				if account.account_type.name == 'Admin':
					return redirect(url_for('admin_department'))
		return redirect(url_for('adminlogout'))
	
	if "username" in session:
		return redirect(url_for('admin_department'))
	return render_template('/log_register/login.html')