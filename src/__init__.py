from flask import Flask
from model import db, User
from flask_login import LoginManager
import os

user = "user"
password = "password"
host = "postgres"
database = "test"
port = "5432"

def create_app():
	app = Flask(__name__, static_url_path="/static")
	app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
		user, password, host, port, database)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	app.env = "development"
	app.app_context().push()

	loginManager = LoginManager()
	loginManager.init_app(app)
	app.secret_key = os.urandom(24)
	
	@loginManager.user_loader
	def load_user(user_id):
		return User.get(user_id)
	
	db.init_app(app)
	db.create_all()
	return app