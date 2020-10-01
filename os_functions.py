import os
from pathlib import Path

def make_directory_tree(pathname):
	"""
	Creats  hierarchical paths
	"""
	path = Path(pathname)
	path.mkdir(parents = True, exist_ok = True)


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


if __name__ == "__main__":
	pass