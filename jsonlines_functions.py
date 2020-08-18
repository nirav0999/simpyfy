import jsonlines
import json


def read_json_objects(filepath, verbose = True):
	"""
	Read a jsonlines object
	"""
	objects = [] 
	
	if verbose == True : print('Reading on ',filepath,'.......')

	with jsonlines.open(filepath) as reader:
		for obj in reader:
			objects.append(obj)
	
	if verbose == True:
		for obj in objects:
			print(obj)

	return objects

def write_json_object(jsonobject, filepath, verbose = True):
	"""
	Write a jsonlines object
	"""
	if verbose == True : print('Writing on ',filepath,'.......')
	
	with jsonlines.open(filepath, mode = 'w') as writer:
		writer.write(jsonobject)

	if verbose == True : print('Done writing')

def append_json_object(jsonobject,filepath,  verbose = True):
	"""
	Append a jsonlines object
	"""
	if verbose == True : print('Appending on ',filepath,'.......')
	
	with jsonlines.open(filepath, mode = 'a') as writer:
		writer.write(jsonobject)

	if verbose == True : print('Done append')