from flask import Flask, render_template, request, redirect, url_for, session, flash
from eventcalendar.app import app
import bcrypt
from datetime import timedelta

from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType

@app.route('/studentlogout')
def studentlogout():
	session.clear()
	flash('The username or password not valid.')
	return redirect(url_for('student_login'))



@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
	#can delete this and change info from POST method
	# if request.method == 'GET':
	# 	return render_template('/log_register/login.html')
	
	if request.method == 'POST':
		session.permanent = True
		student_username = request.form['username']
		password = request.form['password']
		session["student_username"] = student_username

		account = Account.query.filter_by(username = student_username, status="active").first()
		if account:
			if bcrypt.checkpw(password.encode('UTF-8'), account.password.encode('UTF-8')):
				if account.account_type.name == 'Student':
					return redirect(url_for('student_event'))
		return redirect(url_for('studentlogout'))
	
	if "student_username" in session:
		return redirect(url_for('student_event'))
	return render_template('/log_register/student_login.html')



		# else:
		# 	if error is not None:
		# 		session.clear()
		# 		# session["account_id"] = account.id["id"]