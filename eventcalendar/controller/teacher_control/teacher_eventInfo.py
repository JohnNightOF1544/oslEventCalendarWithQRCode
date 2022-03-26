from flask import Flask, render_template, redirect, request, session, url_for
from eventcalendar.app import app
from eventcalendar.models.account import Account
from eventcalendar.models.account_type import AccountType
from eventcalendar.models.event import Event
from eventcalendar.models.department import Department
from eventcalendar.models.venue import Venue


@app.route('/teacher/event_info', methods=['GET', 'POST'])
def teacher_event_info():
    if "teacher_username" in session:
        teacher_username = session['teacher_username']
        if request.method == 'GET':



            test = Event.query.order_by(Event.id.desc()).all()
            


            teacherAccounttypes = AccountType.query.filter(AccountType.id.endswith('2')).all()



            return render_template('/teacher/teacher_template/teacher_eventInfo.html', test=test, teacher_username=teacher_username, teacherAccounttypes=teacherAccounttypes)
    
    else:
        return redirect(url_for('teacher_login'))




