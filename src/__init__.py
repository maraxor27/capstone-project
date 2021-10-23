from flask import Flask
from model import db

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
	app.app_context().push()
	db.init_app(app)
	db.create_all()
	return app