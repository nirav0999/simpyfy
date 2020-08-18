import json
import csv
import collections
import pickle
import os

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

if __name__ == '__main__':
	pass