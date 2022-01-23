from flask import Blueprint, request, abort
from dataAccessLayer.users import getAllUsers, createUser, getUser, removeUser, replaceUser
from dataAccessLayer import DataAccessLayerException
from flask_restx import Namespace, Resource, fields

#comment test
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


# Current version of the api
userNamespace = Namespace("users", path="/users")
userParser = userNamespace.model('User', {
		"email": fields.String(default="name@email.com", required=True),
		"password": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
		"userType": fields.String(default="USER", required=True, 
			description="Must be one of the following ['USER', 'OWNER', 'AGENT']"),
	})

userTypes = ['USER', 'OWNER', 'AGENT', 'ADMIN']
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
		try:
			return getAllUsers()
		except DataAccessLayerException as e:
			abort(e.code, e.message)

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	@userNamespace.expect(userParser, validate=True)
	@userNamespace.doc(description="This api endpoint creates a new user")
	@checkUserType
	def post(self):
		try:
			return createUser(request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)


@userNamespace.route("/<int:id>")
@userNamespace.doc(params={"id":"An ID",}, description="ID of a User")
class UserID(Resource):
	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	@userNamespace.doc(description="This api endpoint returns the information for a specific user")
	def get(self, id):
		try:
			return getUser(id)
		except DataAccessLayerException as e:
			abort(e.code, e.message)

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	def delete(self, id):
		try:
			return removeUser(id)
		except DataAccessLayerException as e:
			abort(e.code, e.message)

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	@userNamespace.expect(userParser, validate=True)
	@checkUserType
	def put(self, id):
		try:
			return replaceUser(id, request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)