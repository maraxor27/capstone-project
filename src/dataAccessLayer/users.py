from model import User, db
from model.users import UserSchema
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

def getUser(user_id):
	user = User.query.filter(User.id == user_id).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'id not found')
	return UserSchema().dump(user)

def removeUser(user_id):
	user = User.query.filter(User.id == user_id).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'id not found')
	json = UserSchema().dump(user)
	db.session.delete(user)
	db.session.commit()
	return json

def replaceUser(user_id, json):
	new_user = UserSchema().load(json)
	new_user.id = user_id
	user = User.query.filter(User.id == user_id).one_or_none()
	if user is None:
		raise DataAccessLayerException(400, 'id not found')
	user = new_user
	db.session.commit()
	return UserSchema().dump(user)