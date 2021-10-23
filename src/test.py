from model import db
from model.users import User


def test1():
	# db.session.add(
	# 	User(email="test.test@test.com", 
	# 	password="test_test"))
	# db.session.commit()
	clearUser()
	users = User.query.all()
	for user in users:
		print(user)

def clearUser():
	for user in User.query.all():
		db.session.delete(user)
	db.session.commit()

