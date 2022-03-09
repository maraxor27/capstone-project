from ..decompiler import decompileLines

from .exception import DataAccessLayerException

def decompile(json):
	code = json.get('assembly')
	return {'cCode':decompileLines(code.split('\n'))}

