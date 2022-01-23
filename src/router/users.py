from flask import Blueprint, request, abort
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user

from ..dataAccessLayer import getAllUsers, createUser, getUser, \
	removeUser, updateUser,	DataAccessLayerException

# Current version of the api
userNamespace = Namespace("users", path="/users")

userParser = userNamespace.model('User', {
		"username": fields.String(default="username", required=True),
		"password": fields.String(default="password123", required=True, 
			description="Will eventually be the hashed password"),
		"email": fields.String(default="firstname.lastname@email.com", required=True),
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
	@userNamespace.expect(userParser)
	def put(self, id):
		try:
			return updateUser(id, request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)
