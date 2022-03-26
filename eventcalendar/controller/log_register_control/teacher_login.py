from flask import Flask, render_template, request, redirect, url_for, session, flash
from eventcalendar.app import app
import bcrypt
from datetime import timedelta

from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType

@app.route('/teacherlogout')
def teacherlogout():
	session.clear()
	flash('The username or password not valid.')
	return redirect(url_for('teacher_login'))

@app.route('/teacher_login', methods=['GET', 'POST'])
def teacher_login():
	#can delete this and change info from POST method
	# if request.method == 'GET':
	# 	return render_template('/log_register/login.html')

	if request.method == 'POST':
		session.permanent = True
		teacher_username = request.form['username']
		password = request.form['password']
		session["teacher_username"] = teacher_username

		account = Account.query.filter_by(username = teacher_username, status="active").first()
		if account:
			if bcrypt.checkpw(password.encode('UTF-8'), account.password.encode('UTF-8')):
				if account.account_type.name == 'Teacher':
					return redirect(url_for('teacher_event'))
		return redirect(url_for('teacherlogout'))
		
	if "teacher_username" in session:
		return redirect(url_for('teacher_event'))
	return render_template('/log_register/teacher_login.html')