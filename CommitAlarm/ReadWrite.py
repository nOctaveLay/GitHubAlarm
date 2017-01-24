#to change the file/string by using json to python.
import json
#maybe not useful. sorry
from HTTPBA import *
#<filename>->jsonfile transfer python
def readConfig(filename) :
	f = open(filename, 'r')
	debug = open("debug.txt",'w')
	temp = f.read()
	debug.write(temp)
	js = json.loads(temp)
	f.close()
	debug.close()
	return js

#save the data
def writeConfig(filename,data) :
	f = open(filename,'w')
	for x in data:
		f.write(str(x))
		f.write("\n")
	f.close()
	