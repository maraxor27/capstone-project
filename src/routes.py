from flask import send_from_directory, send_file, request, abort
import io
import os
from . import app
from werkzeug.utils import secure_filename


@app.route("/")
def home():
	return send_from_directory("templates", "home.html")

@app.route("/signUp")
def signUp():
	return send_from_directory("templates", "signUp.html")

@app.route("/about")
def about():
	return send_from_directory("templates", "about.html")

# TODO: this route should require login and only be available to ADMIN and AGENT
@app.route("/userMain")
def userMain():
	return send_from_directory("templates", "userMain.html")

	
# TODO: this route should only be accessible by user and owner
# @app.route("/property/<int:id>")
# def propertyView(id):
# 	return send_from_directory("templates", "viewProperty.html")

