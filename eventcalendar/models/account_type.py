from eventcalendar.app import db

class AccountType(db.Model):
	__tablename__ = "account_type"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

	def __init__(self, name):
		self.name = name