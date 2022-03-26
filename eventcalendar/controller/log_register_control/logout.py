from flask import Flask, redirect, url_for, session
from eventcalendar.app import app
from datetime import timedelta

@app.route('/logout')
def logout():
	session.clear()
	# session.pop("admin_username", None)
	return redirect(url_for('admin_login'))

@app.route('/student_logout')
def student_logout():
	session.clear()
	# session.pop("student_username", None)
	return redirect(url_for('student_login'))


@app.route('/teacher_logout')
def teacher_logout():
	session.clear()
	# session.pop("student_username", None)
	return redirect(url_for('teacher_login'))