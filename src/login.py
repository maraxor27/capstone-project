from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required
from model import User

loginBlueprint = Blueprint("loginStuff", __name__, url_prefix="/")

@loginBlueprint.route('/login', methods=['POST'])
def login():
	if request is None or request.json is None:
		print("Empty request", flush=True)
		return '400'
	print("Request: ", request.json, flush=True)
	if request.json['email'] is None or request.json['password'] is None:
		print("Email or password missing", flush=True)
		return '400'
	user = User.query.filter(User.email==request.json['email'] and \
		User.password==request.json['password']).one_or_none()
	if user is None:
		print("No user found", flush=True)
		return '400'
	login_user(user)
	return '200'

@loginBlueprint.route('/logout')
@login_required
def logout():
	logout_user()
	return '200'