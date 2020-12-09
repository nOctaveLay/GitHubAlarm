import json
from HTTPBA import *
CONFIG_FILE="internetfile.txt" #hidden
CONFIG={}

#<filename>->jsonfile transfer python
def readConfig(filename:str) :
	with open(file=filename, mode='r') as f:
		temp = f.read().replace('\'','')[1:]
		js = json.loads(temp)
	return js

#save the data
def writeConfig(filename:str,data:list) :
	string = ""
	for x in data:
		string += x + "\n"
	with open(file=filename, mode='w') as f:
		f.write(string)