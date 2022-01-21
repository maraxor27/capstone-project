from flask import send_from_directory, send_file, request, abort
import io
import os
from . import app
from werkzeug.utils import secure_filename


@app.route("/")
def home():
	return send_from_directory("templates", "home.html")

@app.route("/account")
def accountView():
	return send_from_directory("templates", "accountView.html")

# TODO: this route should require login and only be available to ADMIN and AGENT
@app.route("/accountCreator")
def accountCreator():
	return send_from_directory("templates", "accountCreator.html")

@app.route("/property")
def propertiesView():
	return send_from_directory("templates", "viewProperties.html")

@app.route("/OwnerProperty")
def ownerPropertiesView():
	return send_from_directory("templates", "ownerViewProperties.html")

@app.route("/propertyCreator")
def propertyCreator():
	return send_from_directory("templates", "addProperty.html")

@app.route("/visitHistory")
def visitHistory():
	return send_from_directory("templates", "viewVisitHistory.html")

@app.route("/confirmRent")
def confirmRent():
	return send_from_directory("templates", "confirm.html")
	
# TODO: this route should only be accessible by user and owner
# @app.route("/property/<int:id>")
# def propertyView(id):
# 	return send_from_directory("templates", "viewProperty.html")

