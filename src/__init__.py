from flask import Flask
from flask_login import LoginManager
import os

from .model import * 
from .router import *


user = "user"
password = "password"
host = "postgres"
database = "test"
port = "5432"

def create_flask_app():	
	app = Flask(__name__, static_url_path="/static")
	app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
		user, password, host, port, database)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# max out the upload size to 5 MB
	app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

	app.env = "development"
	app.app_context().push()

	loginManager = LoginManager()
	loginManager.init_app(app)
	app.secret_key = os.urandom(24)
	
	@loginManager.user_loader
	def load_user(user_id):
		user = User.query.filter(User.id==user_id).one_or_none()
		return user
	
	db.init_app(app)
	migrate.init_app(app, db)
	db.create_all()

	# if no Admin exist, create a default one
	if (User.query.count() == 0):
		admin = User(username="Admin", password="password")
		db.session.add(admin)
		db.session.commit()

	app.register_blueprint(router.apiv2Blueprint)
	app.register_blueprint(loginBlueprint)	
	return app


if __name__ == "myapp":
	app = create_flask_app()

	from .routes import *