#to change the file/string by using json to python.
import json
#maybe not useful. sorry
from HTTPBA import *

#<filename>->jsonfile transfer python
def readConfig(filename) :
	f = open(filename, 'r')
	# check where I am wrong.
	debug = open("debug.txt",'w')
	temp = f.read()
	#delete dumps
	temp = temp[2:len(temp)-1]
	#change the json -> because it is not accepted in python "json"
	temp= temp.replace("\\\\","\\")
	temp = temp.replace("\\\\\\\\","\\\\")
	temp = temp.replace("\\\'","\'")
	temp = temp.replace("`","")
	print(temp)
	debug.write(temp)
	js = json.loads(temp)
	f.close()
	debug.close()
	return js

#String -> jsonfile // temporary
# def changeJSON(textname):
# 	temp = textname.strip("\'b")
# 	temp = temp[1:]
# 	js = json.loads()
# 	return js

#String -> can show clearly. 
def show_clear(textname):
	f = open("clear","w")
	temp = textname
	temp = temp.replace("{","\n{")
	temp = temp.replace("[","\n[")
	temp = temp.replace(",",",\n")
	f.write(temp)
	f.close()

#save the data
def writeConfig(filename,data) :
	f = open(filename,'w')
	for x in data:
		f.write(str(x))
		f.write("\n")
	f.close()
	