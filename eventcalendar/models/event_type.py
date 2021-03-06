from eventcalendar.app import db

class EventType(db.Model):
	__tablename__ = "event_type"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255), nullable=False)


	def __init__(self, name, description):
		self.name = name
		self.description = description