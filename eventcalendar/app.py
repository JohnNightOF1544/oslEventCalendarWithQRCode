import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('eventcalendar',instance_relative_config = True, static_folder='static', template_folder='templates')
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from eventcalendar.controller.log_register_control import register, login, logout, teacher_login, student_login
from eventcalendar.controller.homePage_control import home
from eventcalendar.controller.admin_control import department, venue, account, event_type, event, manage_event, request_event, student_request_pending, qrcode
from eventcalendar.controller.student_control import student_event, student_eventInfo
from eventcalendar.controller.teacher_control import teacher, teacher_management_event, teacherRequestpage, teacher_eventInfo


db.create_all()
# it is need for the relationship of the tables
