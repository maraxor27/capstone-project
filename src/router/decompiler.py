from flask import Blueprint, request, abort
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user

from ..dataAccessLayer import DataAccessLayerException, decompile

decompilerNamespace = Namespace("decompiler", path="/decompiler")

decompilerParser = decompilerNamespace.model('DecompilerJSON',{
		"assembly": fields.String(
			default="test:\n\tincb\n\trts", 
			required=True),
		"arch": fields.String(default="68HC12"),
	})

@decompilerNamespace.route("")
class DecompilerAPI(Resource):
	@decompilerNamespace.response(200, 'Success')
	@decompilerNamespace.expect(decompilerParser, validate=True)
	@decompilerNamespace.doc(description="This endpoint takes assembly code and return c code")
	def post(self):
		try:
			return decompile(request.json)
		except DataAccessLayerException as e:
			abort(e.code, e.message)