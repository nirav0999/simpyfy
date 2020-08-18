import csv
import h5py

def convertToJsonNumpy(filepath):
	dict1 = {} 
	hf = h5py.File(filepath)	
	for key in hf.keys():
		data = hf.get(key).value
		dict1[key] = data
	return dict1
