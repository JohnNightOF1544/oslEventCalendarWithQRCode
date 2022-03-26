from eventcalendar.app import db
from sqlalchemy import ForeignKey
from datetime import datetime

class EventParticipant(db.Model):
	__tablename__ = "event_participant"
	id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.String(60), nullable=False)
	datetime = db.Column(db.DateTime(timezone = True), default=datetime.now()) 
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

	account = db.relationship('Account', backref='event_participant', lazy=True)
	event = db.relationship('Event', backref='event_participant', lazy=True)
	

	def __init__(self,  status, datetime):
		self.status = status
		self.datetime = datetime