import json
from HTTPBA import *
CONFIG_FILE="internetfile.txt" #hidden
CONFIG={}
#<filename>->jsonfile transfer python
def readConfig(filename) :
	f = open(filename, 'r')
	temp = f.read().replace('\'','')
	temp = temp[1:]
	js = json.loads(temp)
	f.close()
	return js

#save the data
def writeConfig(filename,data) :
	f = open(filename,'w')
	for x in data:
		f.write(str(x))
		f.write("\n")
	f.close()
	