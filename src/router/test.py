from flask import Blueprint

testBlueprint = Blueprint("test", __name__, url_prefix="/test")

@testBlueprint.route('/', methods=['GET'])
def test():
	return "{test: 'test'}"