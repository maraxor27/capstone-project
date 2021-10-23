from . import db

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100))
	password = db.Column(db.String(255))

	def __repr__(self):
		return f"User:{self.id}<email: {self.email}, password:{self.password}>"
