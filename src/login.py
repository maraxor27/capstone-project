from flask import Blueprint, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from model import User
from model.users import UserSchema

loginBlueprint = Blueprint("loginStuff", __name__, url_prefix="/")

@loginBlueprint.route('/login', methods=['POST'])
def login():
	if current_user is not None and current_user.is_authenticated:
		return UserSchema().dump(current_user)
	if request is None or request.json is None:
		return abort(400, "Empty request")
	# print("Request: ", request.json, flush=True)
	if request.json.get('email') is None or request.json.get('password') is None:
		return abort(400, "Email or password is missing")
	user = User.query.filter(User.email==request.json['email'] and \
		User.password==request.json['password']).one_or_none()
	if user is None:
		return abort(400, "User with matching credential not found")
	login_user(user)
	return UserSchema().dump(user)

@loginBlueprint.route('/logout')
@login_required
def logout():
	logout_user()
	return 'ok'