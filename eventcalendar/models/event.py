from eventcalendar.app import db
from sqlalchemy import ForeignKey
from datetime import datetime

class Event(db.Model):
	__tablename__ = "event"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	datetime_start = db.Column(db.DateTime(timezone = True), default=datetime.now())
	datetime_end = db.Column(db.DateTime(timezone = True), default=datetime.now())
	status = db.Column(db.String(100), nullable=False)
	event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)
	venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
	department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

	venue = db.relationship('Venue', backref='event')
	event_type = db.relationship('EventType', backref='event')
	department = db.relationship('Department', backref='event')


	def __init__(self, name, datetime_start, datetime_end, status):
		self.name = name
		self.datetime_start = datetime_start
		self.datetime_end = datetime_end
		self.status = status