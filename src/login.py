from flask import Blueprint, request, abort
from flask_login import login_user, logout_user, login_required
from model import User

loginBlueprint = Blueprint("loginStuff", __name__, url_prefix="/")

@loginBlueprint.route('/login', methods=['POST'])
def login():
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
	return 'ok'

@loginBlueprint.route('/logout')
@login_required
def logout():
	logout_user()
	return 'ok'