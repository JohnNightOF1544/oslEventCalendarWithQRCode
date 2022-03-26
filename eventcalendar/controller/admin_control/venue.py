from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.venue import Venue

@app.route('/admin/venues', methods=['POST', 'GET'])
def admin_venue():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			venueVenues = Venue.query.order_by(Venue.id).all()
			venueAccounts = Account.query.filter(Account.id.endswith('5')).all()
			venueAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_venue.html', venueVenues=venueVenues, username=username, venueAccounttypes=venueAccounttypes)

		if request.method == 'POST':
			venue_name = request.form['venueName']
			venue_description = request.form['venueDescription']
			new_venue = Venue(name=venue_name, description=venue_description)
			try:
				db.session.add(new_venue)
				db.session.commit()
				return redirect('/admin/venues')
			except:
				return 'There are no words in the table'
	else:
		
		return redirect(url_for('admin_login'))

@app.route('/admin/venues/<int:id>', methods=['UPDATE', 'DELETE', 'GET'])
def manage_admin_venue(id):
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			venue = Venue.query.get_or_404(id)
			if venue:
				return {"id": venue.id, "name": venue.name, "description": venue.description}
			else:
				return {"message": "Venue not found"}

		if request.method == 'DELETE':
			deleteVenue = Venue.query.get_or_404(id)
			try:
				db.session.delete(deleteVenue)
				db.session.commit()
				return {"message": "Venue successfully deleted"},200
			except:
				return 'There are a problem deleting'

		if request.method == 'UPDATE':
			updateVenue = Venue.query.get_or_404(id)
			try:
				updateVenue.name = request.form['name']
				updateVenue.description = request.form['description']
				db.session.commit()
				return dict(id = id, name = updateVenue.name, description = updateVenue.description),200
			except:
				return 'There are a problem updating it'
	else:
		
		return redirect(url_for('admin_login'))


	



# username = request.cookies.get('username')
# 	re = make_response(render_template('OSLDash.html', username = username))
# 	return re

# entries = Department.query.order_by(Department.name, Department.description).all()