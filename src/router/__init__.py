from flask import Blueprint
from .test import testBlueprint

apiBlueprint = Blueprint("api", __name__, url_prefix="/api/v1")
apiBlueprint.register_blueprint(testBlueprint)