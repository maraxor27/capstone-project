from flask import Blueprint, request, abort
from model import User, db
from model.users import UserSchema
from flask_restx import Namespace, Resource, fields

#depricated version of the api
usersBlueprint = Blueprint("users", __name__, url_prefix="/users")

@usersBlueprint.route('/', methods=['GET'])
def get_users():
	users = User.query.all()
	json = UserSchema().dump(users, many=True)
	return {"users" : json}

@usersBlueprint.route('/', methods=['POST'])
def post_users():
	user = UserSchema().load(request.json)
	print(user)
	return 201

@usersBlueprint.route('/<int:id>', methods=['GET'])
def get_user(id):
	user = User.query.filter(User.id == id).one()
	print(user, flush=True)
	json = UserSchema().dump(user)
	return {"user" : json}


userNamespace = Namespace("users", path="/users")
userParser = userNamespace.model('User', {
		"email": fields.String(default="name@email.com", required=True),
		"password": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
		"userType": fields.String(default="USER", required=True, 
			description="Must be one of the following ['USER', 'OWNER', 'AGENT']"),
	})

userTypes = ["USER", 'OWNER', 'AGENT']
def checkUserType(func): #decorator that checks the userType
	def inner(*args, **kwargs):
		user_type = request.json.get('userType')
		if user_type in userTypes:
			return func(*args, **kwargs)
		abort(400, 'Bad userType')
	return inner

@userNamespace.route("/")
class Users(Resource):
	@userNamespace.response(200, 'Success')
	@userNamespace.doc(description="This api endpoint returns all the user of the application.Once testing is over, this should be removed")
	def get(self):
		users = User.query.all()
		json = UserSchema().dump(users, many=True)
		return {"users" : json}

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalide request')
	@userNamespace.expect(userParser, validate=True)
	@userNamespace.doc(description="This api endpoint creates a new user")
	@checkUserType
	def post(self):
		user = UserSchema().load(request.json)
		if User.query.filter(User.email == user.email).count() != 0:
			abort(400, 'Email already used')
		db.session.add(user)
		db.session.commit()
		json = UserSchema().dump(user)
		return json

@userNamespace.route("/<int:id>")
@userNamespace.doc(params={"id":"An ID",}, description="ID of a User")
class UserID(Resource):
	@userNamespace.response(200, 'Success')
	@userNamespace.response(404, 'Not Found')
	@userNamespace.doc(description="This api endpoint returns the information for a specific user")
	def get(self, id):
		user = User.query.filter(User.id == id).one_or_none()
		if user is None:
			abort(404, 'id doesn\'t not found')
		json = UserSchema().dump(user)
		return {"user" : json}

	@userNamespace.response(200, 'Success')
	@userNamespace.response(404, 'Not Found')
	def delete(self, id):
		user = User.query.filter(User.id == id).one_or_none()
		if user is None:
			abort(404, 'id doesn\'t not found')
		json = UserSchema().dump(user)
		db.session.delete(user)
		db.session.commit()
		return {"user" : json}

	@userNamespace.response(200, 'Success')
	@userNamespace.response(404, 'Not Found')
	@userNamespace.expect(userParser, validate=True)
	@checkUserType
	def put(self, id):
		user = User.query.filter(User.id == id).one_or_none()
		if user is None:
			abort(404, 'id doesn\'t not found')
		user.email = request.json.email
		user.password = request.json.password
		user.userType = request.json.userType
		db.session.commit()
		json = UserSchema().dump(user)
		return {"user" : json}


