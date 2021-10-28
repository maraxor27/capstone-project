from flask import Blueprint, request
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
		"email": fields.String(default="name@email.com"),
		"password": fields.String(default="password123", description="Will eventually be the hashed password"),
		"userType": fields.String(default="USER"),
	})

@userNamespace.route("/")
class Users(Resource):
	@userNamespace.doc(description="This api endpoint returns all the user of the application.Once testing is over, this should be removed")
	def get(self):
		print("Type of User: ",type(User), flush=True)
		users = User.query.all()
		print(users, flush=True)
		json = UserSchema().dump(users, many=True)
		return {"users" : json}

	@userNamespace.expect(userParser)
	@userNamespace.doc(description="This api endpoint creates a new user")
	def post(self):
		user = UserSchema().load(request.json)
		if User.query.filter(User.email == user.email).count() != 0:
			return '400'
		db.session.add(user)
		db.session.commit()
		json = UserSchema().dump(user)
		return json

@userNamespace.route("/<int:id>")
@userNamespace.doc(params={"id":"An ID",}, description="ID of a User")
class UserID(Resource):
	@userNamespace.doc(description="This api endpoint returns the information for a specific user")
	def get(self, id):
		user = User.query.filter(User.id == id).one()
		print(user, flush=True)
		json = UserSchema().dump(user)
		return {"user" : json}

	def delete(self, id):
		user = User.query.filter(User.id == id).one()
		print(user, flush=True)
		json = UserSchema().dump(user)
		db.session.delete(user)
		db.session.commit()
		return {"user" : json}