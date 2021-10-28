import flask_sqlalchemy
import flask_marshmallow
import enum

db = flask_sqlalchemy.SQLAlchemy()
ma = flask_marshmallow.Marshmallow()

class UserType(enum.Enum):
	USER = 0
	OWNER = 1
	AGENT = 2

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100))
	password = db.Column(db.String(255))
	userType = db.Column(db.Integer)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True #no activation required in this case

	def is_anonymous(self):
		return False

	def get_id(self):
		return id

	def __repr__(self):
		return f"""User:{self.id}<email: {self.email}, password:{self.password}, 
		type:{self.userType}>"""