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

@app.route("/userMain")
def userMain():
	return send_from_directory("templates", "userMain.html")

@app.route("/terms")
def terms():
	return send_from_directory("templates", "terms.html")

