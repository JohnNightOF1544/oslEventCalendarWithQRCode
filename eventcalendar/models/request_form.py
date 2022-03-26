from eventcalendar.app import db
from datetime import datetime

class RequestForm(db.Model):
	__tablename__ = "request_form"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255), nullable=False)
	datetime_start = db.Column(db.DateTime(timezone = True), default=datetime.now())
	datetime_end = db.Column(db.DateTime(timezone = True), default=datetime.now())
	request_created = db.Column(db.DateTime(timezone = True), default=datetime.now())
	department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

	department = db.relationship('Department', backref='request_form')
	
	def __init__(self, name, description, datetime_start, datetime_end):
		self.name = name
		self.description = description
		self.datetime_start = datetime_start
		self.datetime_end = datetime_end