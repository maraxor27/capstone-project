from . import ma
from . import User
from marshmallow import post_load

class UserSchema(ma.Schema):
	class Meta:
		model = User
		fields = ("id", "email", "password", "userType", "_links")

	_links = ma.Hyperlinks({
			"self": ma.URLFor("apiv2.users_user_id", values=dict(id="<id>")),
			"collection": ma.URLFor("apiv2.users_users"),
		})

	@post_load
	def make_user(self, data, **kwargs):
		return User(**data)