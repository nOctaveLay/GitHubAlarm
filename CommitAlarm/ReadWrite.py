#to change the file/string by using json to python.
import json
#maybe not useful. sorry
from HTTPBA import *
#<filename>->jsonfile transfer python
def readConfig(filename:str) :
	with open(file=filename, mode='r') as f:
		temp = f.read().replace('\'','')[1:]
		js = json.loads(temp)
	return js

#save the data
def writeConfig(filename:str,data:list) :
	string = ""
	string += f"{x}\n" for x in data
	with open(file=filename, mode='w') as f:
		f.write(string)