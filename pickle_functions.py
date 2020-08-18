import pickle


#-------------------------Pickle Functions-------------------------------------------------------
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

if __name__ == "__main__":
	pass