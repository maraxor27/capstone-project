from flask import Blueprint, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import and_

from ..model import User, UserSchema


loginBlueprint = Blueprint("loginStuff", __name__, url_prefix="/")

def userTypes_required_decorator_factory(types):
	def decorator(func):
		def inner(*args, **kwargs):
			if current_user.userType in types:
				return func(*args, **kwargs)
			return abort(401, 'Unauthorized')
		return inner
	return decorator

@loginBlueprint.route('/login', methods=['POST'])
def login():
	if current_user is not None and current_user.is_authenticated:
		return UserSchema().dump(current_user)
	if request is None or request.json is None:
		return abort(400, "Empty request")
	if request.json.get('email') is None or request.json.get('password') is None:
		return abort(400, "email or password is missing")
	user = User.query.filter(and_(User.email==request.json['email'],
		User.password==request.json['password'])).one_or_none()
	if user is None:
		return abort(400, "User with matching credential not found")
	login_user(user)
	return UserSchema().dump(user)

@loginBlueprint.route('/logout')
@login_required
def logout():
	logout_user()
	return 'ok'