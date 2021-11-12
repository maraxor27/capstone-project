from flask import Blueprint
from .users import usersBlueprint, userNamespace
from flask_restx import Api

# Depricated do not extend api/v1
apiv1Blueprint = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1Blueprint.register_blueprint(usersBlueprint)


apiv2Blueprint = Blueprint("apiv2", __name__, url_prefix="/api/v2")
api = Api(apiv2Blueprint, version='2.0', doc='/doc/')
api.add_namespace(userNamespace)