from flask import Flask, render_template, redirect, url_for, session, request, send_file
from eventcalendar.app import app
from eventcalendar.models.account_type import AccountType

@app.route('/QR_Code_Generater')
def qrhome():
    if "username" in session:
        username = session['username']
        if request.method == 'GET':
            eventAccounttypes = AccountType.query.filter(AccountType.id.endswith('1')).all()
            return render_template('/admin/osl_template/osl_qrIndex.html', username=username, eventAccounttypes=eventAccounttypes)
    else:
        return redirect(url_for('admin_login'))
