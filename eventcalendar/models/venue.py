from eventcalendar.app import db

class Venue(db.Model):
	__tablename__ = "venue"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	description = db.Column(db.String(255), nullable=False)


	def __init__(self, name, description):
		self.name = name
		self.description = description