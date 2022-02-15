from flask_login import current_user
from sqlalchemy import and_

from ..model import User, db, UserSchema
from .exception import DataAccessLayerException


def getAllUsers():
	users = User.query.all()
	return UserSchema().dump(users, many=True)

def createUser(json):
	user = UserSchema().load(json)
	if User.query.filter(User.email == user.email).count() != 0:
		raise DataAccessLayerException(400, 'Email already used')
	db.session.add(user)
	db.session.commit()
	return UserSchema().dump(user)

def getUser(user_email):
	user = User.query.filter(User.email == user_email).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'User not found')
	return UserSchema().dump(user)

def removeUser(user_email):
	user = User.query.filter(User.email == user_email).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'User not found')
	user.deleted = True
	db.session.commit()
	return UserSchema().dump(user)

def updateUser(user_email, json):
	user = User.query.filter(User.email == user_email).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'User not found')
	
	if user.password != json.get('oldPassword'):
		raise DataAccessLayerException(400, 'old password doesn\'t match')

	# Currently no one should be able to change their userType
	buffer = json.get('password')
	if buffer is not None:
		user.password = buffer
	db.session.commit()
	return UserSchema().dump(user)