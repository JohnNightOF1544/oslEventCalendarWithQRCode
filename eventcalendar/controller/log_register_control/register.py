from flask import Flask, flash, render_template, request, redirect, url_for
from eventcalendar.app import app, db
import bcrypt
from datetime import timedelta

from eventcalendar.models.department import Department
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		departments = Department.query.all()
		return render_template('/log_register/registration.html', departments = departments)

	check_username = request.form['username']

	username = Account.query.filter_by(username= check_username).first()
	
	if username:
		return render_template('/log_register/username_taken.html' )

	if request.method == 'POST':
		Fname = request.form['Fname']
		Mname = request.form['Mname']
		Lname = request.form['Lname']
		gender = request.form['gender']
		year_level = request.form['year_level']
		username = request.form['username']

		password = bcrypt.hashpw(request.form['password'].encode('UTF-8'), bcrypt.gensalt(rounds=15))
		account_type = AccountType.query.filter_by(name = "guest").first() #add and info from the database
		department = Department.query.get(request.form['department']) #query info from the database
		new_user = Account(Fname = Fname, Mname = Mname, Lname = Lname, gender = gender, year_level = year_level, username = username, password = password)
		new_user.department = department
		new_user.account_type = account_type

		db.session.add(new_user)
		db.session.commit()
		flash('Needs validation from admin.')
		return redirect(url_for('register'))

