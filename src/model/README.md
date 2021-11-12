# How to add a database table in this project

1. Add db.Model at end of __init__.py of this directory
```python
class Example(db.Model):
	__tablename__ = "example"
	id = db.Column(db.Integer, primary_key=True)
	var_1 = db.Column(db.String(100))

	def __repr(self):
		return "string that represent the databse object"
```

2. Create a new file named after the new class from step 1 (examples.py)

```python
from . import ma

#import class added to __init__.py
from . import Example

from marshmallow import post_load

class ExampleSchema(ma.Schema):
	class Meta:
		model = Example

		# add the name of every datablase db.Column that may be useful in the front end. When not sure, add all of them 
		fields = ("id", "var_1", "_links")

	_links = ma.Hyperlinks({
		# link to the api that need to be exposed by the element
		# apiv2 is the name of the first namespace
		# examples_example_id is the name of the second namespace combined with the name of the class of the desired route.
			"self": ma.URLFor("apiv2.examples_example_id", values=dict(id="<id>")),
		})

	# This is important to ensure the schema is able to create an Example database row from the json received in the request
	@post_load
	def make_user(self, data, **kwargs): 
		return Example(**data)
```