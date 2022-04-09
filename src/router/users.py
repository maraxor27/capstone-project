from flask import Blueprint, request, abort
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user

from ..dataAccessLayer import getAllUsers, createUser, getUser, \
	removeUser, updateUser,	DataAccessLayerException

# Current version of the api
userNamespace = Namespace("users", path="/users")

userParser = userNamespace.model('User', {
		"firstname": fields.String(default="firstname", required=True),
		"lastname": fields.String(default="lastname", required=True),
		"email": fields.String(default="firstname.lastname@email.com", required=True),
		"password": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
	})


# TODO: Restrict the api to only be available for ADMIN and AGENT
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
	def post(self):
		try:
			return createUser(request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)

newPasswordParser = userNamespace.model('NewPassword', {
		"password": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
		"oldPassword": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
	})

@userNamespace.route("/<string:email>")
@userNamespace.doc(params={"email":"An email",}, description="Email of a User")
class UserEmail(Resource):
	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	@userNamespace.doc(description="This api endpoint returns the information for a specific user")
	def get(self, email):
		try:
			return getUser(email)
		except DataAccessLayerException as e:
			abort(e.code, e.message)

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	def delete(self, email):
		try:
			return removeUser(email)
		except DataAccessLayerException as e:
			abort(e.code, e.message)

	@userNamespace.response(200, 'Success')
	@userNamespace.response(400, 'Invalid request')
	@userNamespace.expect(newPasswordParser)
	def put(self, email):
		try:
			return updateUser(email, request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)
