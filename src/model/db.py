import flask_sqlalchemy
import flask_marshmallow
import flask_migrate
import enum
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
ma = flask_marshmallow.Marshmallow()


#TODO: index the database to accelerate the access speed on big request


class User(db.Model):
	__tablename__ = "users"
	email = db.Column(db.String(100), primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	password = db.Column(db.String(255))


	created = db.Column(db.DateTime(timezone=True), default=datetime.now())

	def is_authenticated(self):
		return True

	def is_active(self):
		return True #no activation required in this case

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.email

	def __repr__(self):
		val = f"User:{self.email} <"
		val = val + f"firstname: {self.firstname}, "
		val = val + f"lastname: {self.firstname}, "	
		val = val + f"password: {self.password}, "
		val = val + f"created: {self.created}"
		val = val + ">"
		return val

