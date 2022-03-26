from eventcalendar.app import db

class Department(db.Model):
	__tablename__ = "department"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255), nullable=False)


	def __init__(self, name, description):
		self.name = name
		self.description = description