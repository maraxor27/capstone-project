# How to create data accesslayer for your endpoint

1. Create a file with the name of the database object your endpoint needs to use. In this case: examples.py

```python
from ..model import Example, db, exampleSchema
from .exception import DataAccessLayerException

def getAllExamples():
	examples = Example.query.all()
	return UserSchema().dump(examples, many=True)

def addExample(json):
	example = ExampleSchema().load(json)
	if Example.query.filter(Example.var_1 == example.var_1).count() != 0:
		raise DataAccessLayerException(400, 'var_1 already used')
	db.session.add(example)
	db.session.commit()
	return ExampleSchema().dump(example)
``` 