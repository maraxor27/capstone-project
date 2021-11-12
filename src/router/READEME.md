# How to add an api endpoint

1. Create a new namespace and routes for the endpoint in a new file (In this case, we would create examples.py)
```python
from flask import Blueprint, request, abort
from flask_restx import Namespace, Resource, fields

#import db and the database classes used in this end point.
from dataAccessLayer.examples import getAllExample, addExample
from dataAccessLayer import DataAccessLayerException

exampleNamespace = Namespace("examples", path="/examples")

exampleParser = userNamespace.model('Example', {
		# In this case, var_1 is the name of this field. default= defines the default value in the swagger documentation. required= either True or false is use to know if all json must have this field when an endpoint expect this type of data.
		"var_1": fields.String(default="default", required=True, descript="description of the field"),
	})

# route("/") defines what must be added to the namespace path to reach this endpoint. "/" means nothing must be added.
@exampleNamespace.route("/")
class Examples(Resource):
	# Each http request type can be define by using its name as the function name.
	# HTTP request type [get, post, put, delete, patch, options, head]. For the love of god, please follow the documentation about those request type. For example, get SHOULDN'T add an element to the database. 

	# The response() decorator add to the documentation one response that is possible. It can be use multiple time to document multiple answers.
	@exampleNamespace.response(200, 'Success')
	@exampleNamespace.response(500, 'Internal Error')
	@exampleNamespace.doc(description="Description of what the route does")
	def get(self):
		# This function is only an endpoint. It must call functions from the dataAccessLayer to actually do stuff.
		examples_json = getAllExample()
		return {"examples": examples_json}

	# The expect() decorator is use to ensure that the json in the request as the proper field and that does fields have the proper type. 
	@exampleNamespace.response(200, 'Success')
	@exampleNamespace.response(400, 'Invalid request')
	@exampleNamespace.response(500, 'Internal Error')
	@exampleNamespace.expect(exampleParser, validate=True)
	def post(self):
		# Call the dataAccessLayer to add the 
		example_json = addExample(request.json)
		return example_json

```

2. Add the created Namespace to the api Blueprint (This is done by modifyingn the __init__.py file)
```python
# import the namespace from the file created at step 1
from .examples import exampleNamespace

#this Blueprint will already be in the file 
apiv2Blueprint = Blueprint("apiv2", __name__, url_prefix="/api/v2")
api = Api(apiv2Blueprint, version='2.0', doc='/doc/')

# add the Namespace create in the file from previous step to the api Blueprint 
api.add_namespace(exampleNamespace)

```