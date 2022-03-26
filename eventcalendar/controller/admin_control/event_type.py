from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event_type import EventType

@app.route('/admin/event_types', methods=['POST', 'GET'])
def admin_eventtype():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			eventtypeEventtypes = EventType.query.order_by(EventType.id).all()
			eventtypeAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_event_type.html', eventtypeEventtypes=eventtypeEventtypes, username=username, eventtypeAccounttypes=eventtypeAccounttypes)

		if request.method == 'POST':
			eventtype_name = request.form['eventtypeName']
			eventtype_description = request.form['eventtypeDescription']
			new_event_type = EventType(name=eventtype_name, description=eventtype_description)
			try:
				db.session.add(new_event_type)
				db.session.commit()
				return redirect('/admin/event_types')
			except:
				return 'There are no words in the table'
	else:
		
		return redirect(url_for('admin_login'))

@app.route('/admin/event_types/<int:id>', methods = ['UPDATE', 'DELETE', 'GET'])
def manage_eventtype(id):
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			eventtype = EventType.query.get_or_404(id)
			if eventtype:
				return {"id": eventtype.id, "name": eventtype.name, "description": eventtype.description}
			else:
				return {"message": "Event Type not found"}

		if request.method == 'DELETE':
			deleteEventtype = EventType.query.get_or_404(id)
			try:
				db.session.delete(deleteEventtype)
				db.session.commit()
				return {"message": "Event Type successfully deleted"},200
			except:
				return 'There are a problem deleting'

		if request.method == 'UPDATE':
			updateEventtype = EventType.query.get_or_404(id)
			try:
				updateEventtype.name = request.form['name']
				updateEventtype.description = request.form['description']
				db.session.commit()
				return dict(id = id, name = updateEventtype.name, description = updateEventtype.description),200
			except:
				return 'There are a problem updating it'
	else:
		
		return redirect(url_for('admin_login'))