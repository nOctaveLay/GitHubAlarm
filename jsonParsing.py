

import json

CONFIG_FILE="<filename>" #hidden
CONFIG={}

#<filename>->jsonfile transfer python
def readConfig(filename) :
	f = open(filename, 'r')
	temp = f.read().replace('\'','')
	temp = temp[1:]
	js = json.loads(temp)
	f.close()
	return js

def main() :
	global CONFIG_FILE
	global CONFIG

	CONFIG = readConfig(CONFIG_FILE) #type is list
	while len(CONFIG) != 0:
		rpo = CONFIG.pop() #type is dict
		(openwho,opentype) = (rpo["actor"]["display_login"],rpo["type"])
		(openwhat,createdtime) = (rpo["repo"]["name"],rpo["created_at"].replace("T"," "))
		createdtime = createdtime.replace('Z','')
		print(openwho,opentype,openwhat,createdtime)

if __name__ == "__main__":
	main()
