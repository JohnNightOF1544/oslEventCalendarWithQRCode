from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from eventcalendar.app import app, db

migrate = Migrate(app, db)
manager = Manager(app)


if __name__ == '__main__':
	manager.run()
