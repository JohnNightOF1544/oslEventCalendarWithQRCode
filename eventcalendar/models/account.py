from eventcalendar.app import db
from sqlalchemy import ForeignKey

class Account(db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	Fname = db.Column(db.String(100), nullable=False)
	Mname = db.Column(db.String(100), nullable=False)
	Lname = db.Column(db.String(100), nullable=False)
	gender = db.Column(db.String(7), nullable=False)
	username = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)
	status = db.Column(db.String(100), nullable=False)
	year_level = db.Column(db.Integer, nullable = False)
	department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
	account_type_id = db.Column(db.Integer, db.ForeignKey('account_type.id'))

	department = db.relationship('Department', backref='account')
	account_type = db.relationship('AccountType', backref='account')

	def __init__(self, Fname, Mname, Lname, gender, username, password, year_level):
		self.Fname = Fname
		self.Mname = Mname
		self.Lname = Lname
		self.gender = gender
		self.username = username
		self.password = password
		self.status = "inactive"
		self.year_level = year_level