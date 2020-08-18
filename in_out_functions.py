import json
import csv
import collections
import pickle
import os
import jsonlines

#-------------------------Pickle Functions-----------------------------------
def loadPickleFile(filepath, verbose = True, print_obj = False):
	"""
	Loading a Pickle File
	"""
	if verbose == True : print("Loading the pickle file from",filepath,"...........")
	
	pickle_in = open(filepath,"rb")
	example_dict = pickle.load(pickle_in)

	if verbose == True : print("Loaded the pickle File")
	if print_obj == True : print(example_dict)
	
	return example_dict

def dumpPickleFile(data, filepath, verbose = True, print_obj = False):
	"""
	Dumping a pickle file
	"""
	pickle_out = open(filepath,"wb")
	
	if verbose == True : print("Dumping the Pickle file into ",filepath,"...........")
	
	pickle.dump(data, pickle_out)
	
	if verbose == True : print("Dumped the pickle File")
	if print_obj == True : print(data)

	pickle_out.close() 

#-------------------------JSON Functions-------------------------------------
def dumpJsonFile(dictionary, filepath, verbose = True, print_dict = False):
	"""
	Dump a json file
	"""
	if verbose == True : print("Dumping a dictionary to filepath",filepath,"...............")
	
	with open(filepath,"w+") as jsonFile:
		json.dump(dictionary, jsonFile, indent = 4, sort_keys = True)
	
	if print_dict == True : print(json.dumps(dictionary,indent = 4))
	if verbose == True : print("Dumped Successfully")


def loadJsonFile(filepath, verbose = True, print_dict = False):
	"""
	Load a json file 
	"""
	if verbose == True : print("Loading a dictionary to filepath",filepath,".........")
	dictionary = {}
	
	with open(filepath) as jsonFile:
		dictionary = json.load(jsonFile)
	
	if verbose == True : print("Loaded Successfully")
	if print_dict == True : print(json.dumps(dictionary,indent = 4))

	return dictionary


#-------------------------CSV Functions--------------------------------------
def appendToCSV(row, filepath, verbose = True):
	"""
	Appends a csv 
	"""
	if verbose == True: print(row, 'appending into', filepath, '.........')
	with open(filepath,"a",buffering = 1) as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(row)
	if verbose == True: print('Appended')

def openCSVfile(filepath):
	"""
	Open a csv file
	Returns:  a list of rows of the csv 
	"""
	with open(filepath,"r") as csvfile:
		rows =  csv.reader(csvfile)
		return list(rows)


def csvTojson(csvfile,jsonfile,verbose = True):
	graph = {}
	
	rows = openCSVfile(filepath)
	
	# Removing the header row
	rows = rows[1:]
	
	if verbose == True : print("Making graph....")

	for row in rows:
		source = row[0]
		target = row[1]
		weight = row[2]
		if source not in graph:
			graph[source] = {}
			graph[source][target] = int(weight)
		else:
			graph[source][target] = int(weight)

	if verbose == True : print("Dumping to file.........")
	
	with open(jsonfile,"w") as jsonfile:
		json.dump(graph,jsonfile)
	
	if verbose == True : print("Dumped json file")

#-------------------------Dictionrary Functions------------------------------
def invertDictionary(dictionary,verbose = True):
	"""
	Invert a dictionary by inverting dictionary[key] = value
	by forming a new dictionary newDictionary[value] = key
	Returns the newDictionary
	"""
	newDictionary = {}
	for key in dictionary.keys():
		value = dictionary[key]
		if value in dictionary:
			if verbose == True : print("Cannot Revert Duplicate Values Present...." + "\n" +  "Returned the same dictionary as it is")
			return dictionary
		else:
			newDictionary[value] = key
	
	if verbose == True : print("Successfully Reverted the dictionary")
	
	return newDictionary

def sortDictionary(dictionary,attribute = "k",rev = True,verbose = True):
	"""
	Sort a dictionary either by key or value 
	"""
	od = {}
	if attribute == "k":
		if verbose == True : print("Ordering by key.....")
		od = collections.OrderedDict(sorted(dictionary.items(), key=lambda t: t[0],reverse = rev))  
	elif attribute == "v":
		if verbose == True : print("Ordering by Value.....")
		od = collections.OrderedDict(sorted(dictionary.items(), key=lambda t: t[1],reverse = rev))
	else:
		if verbose == True : print("Invalid ordering by attribute")
	return od

#------------------------OS FUNCTIONS----------------------------------------
def get_directory_list(folderpath,sort = True,verbose = True):
	"""
	Returns a list of directories inside  a directory
	"""
	directory_list = []
	for root,d_names,f_names in os.walk(folderpath):
		for dname in d_names:
			directory_list.append(dname)

	# Sorting the list
	if sort == True : directory_list.sort()
	
	print('Directory list is .....')
	if verbose == True : 
		for d in directory_list: 
			print(d)
	return directory_list

def get_file_list(folderpath,sort = True,verbose = True):
	"""
	Returns a list of files inside a directory
	"""
	file_list = []
	
	for root,d_names,f_names in os.walk(folderpath):
		for fname in f_names:
			file_list.append(fname)
	# Sorting the list
	if sort == True:
		file_list.sort()

	print('File list is .....')
	if verbose == True:
		for file in file_list:
			print(file)

	return file_list



#-----------------------jsonlines-----------------------------------------
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

if __name__ == "__main__":
	pass