#to change the file/string by using json to python.
import json
# from HTTPBA import *

#<filename>->jsonfile transfer python
def readConfig(filename:str) :
	with open(file=filename, mode='rb') as f:
		temp = f.read()
		js = json.loads(temp)
	return js

#save the data
def writeConfig(filename:str,data:list) :
	string = ""
	for x in data:
		string += (x+"\n")
	with open(file=filename, mode='w') as f:
		f.write(string)