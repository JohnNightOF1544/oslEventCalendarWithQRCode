from flask import Flask, render_template, redirect, request, url_for, session
from eventcalendar.app import app, db
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.department import Department

@app.route('/admin/departments', methods=['POST', 'GET'])
def admin_department():
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			departmentDepartments = Department.query.order_by(Department.id).all()
			departmentAccounts = Account.query.filter(Account.id.endswith('1')).all()
			departmentAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
			return render_template('/admin/osl_template/osl_department.html', username=username, departmentDepartments=departmentDepartments, departmentAccounts=departmentAccounts, departmentAccounttypes=departmentAccounttypes)


		if request.method == 'POST':
			department_name = request.form['departmentName']
			department_description = request.form['departmentDescription']
			new_department = Department(name=department_name, description=department_description)
			try:
				db.session.add(new_department)
				db.session.commit()
				return redirect('/admin/departments')
			except:
				return 'There are no words in the table'
	else:

		return redirect(url_for('admin_login'))
		

@app.route('/admin/departments/<int:id>', methods = ['UPDATE', 'DELETE','GET'])
def manage_admin_department(id):
	if "username" in session:
		username = session['username']
		if request.method == 'GET':
			department = Department.query.get_or_404(id)
			if department:
				return {"id": department.id, "name": department.name, "description": department.description}
			else:
				return {"message": "Department not found"}

		if request.method == 'DELETE':
			deleteDepartment = Department.query.get_or_404(id)
			try:
				db.session.delete(deleteDepartment)
				db.session.commit()
				return {"message": "department successfully deleted"},200
			except:
				return 'There are a problem deleting'

		if request.method == 'UPDATE':
			updateDepartment = Department.query.get_or_404(id)
			try:
				updateDepartment.name = request.form['name']
				updateDepartment.description = request.form['description']
				db.session.commit()
				return dict(id = id, name = updateDepartment.name, description = updateDepartment.description ),200
			except:
				return 'There are a problem updating it'
	else:
		
		return redirect(url_for('admin_login'))