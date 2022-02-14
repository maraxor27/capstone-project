from marshmallow import post_load, post_dump
from .db import ma, User

class UserSchema(ma.Schema):
	class Meta:
		model = User
		fields = ("password", 
			"email", "created", "_links")

	_links = ma.Hyperlinks({
			"collection": ma.URLFor("apiv2.users_users")
		})


	@post_dump
	def hidePassword(self, data, **kwargs):
		data['password'] = '*' * len(data['password'])
		return data

	@post_load
	def make_user(self, data, **kwargs):
		return User(**data)