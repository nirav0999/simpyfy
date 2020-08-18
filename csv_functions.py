import csv
import json

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

if __name__ == '__main__':
	pass