from flask import Flask, send_from_directory, Blueprint
from router import apiBlueprint

#marshmallow does object serialization may be usefull later 
from flask_marshmallow import Marshmallow

from __init__ import create_app

app = create_app()

ma = Marshmallow(app)

@app.route("/")
def hello():
	return send_from_directory("templates", "index.html")

# from test import test1

# test1()

app.register_blueprint(apiBlueprint)
app.run(host="0.0.0.0", port="5000", debug=True)