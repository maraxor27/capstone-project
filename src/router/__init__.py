from flask import Blueprint
from flask_restx import Api

from .login import loginBlueprint 
from .users import userNamespace


apiv2Blueprint = Blueprint("apiv2", __name__, url_prefix="/api/v2")
api = Api(apiv2Blueprint, version='2.0', doc='/doc/')
api.add_namespace(userNamespace)