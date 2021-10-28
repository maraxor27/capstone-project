from flask import Flask, send_from_directory, Blueprint, request
from router import apiv1Blueprint, apiv2Blueprint
#marshmallow does object serialization may be usefull later 
from flask_marshmallow import Marshmallow
from __init__ import create_app
from login import loginBlueprint
from model import User


if __name__ == "__main__":
	app = create_app()

	@app.route("/")
	def hello():
		return send_from_directory("templates", "index.html")

	app.register_blueprint(apiv1Blueprint)
	app.register_blueprint(apiv2Blueprint)
	app.register_blueprint(loginBlueprint)
	app.run(host="0.0.0.0", port="5000", debug=True)