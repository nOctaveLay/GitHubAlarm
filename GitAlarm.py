from HTTPBA import *
from ReadWrite import *
from Changeform import *

def main() :
	global CONFIG_FILE
	global CONFIG
	saveData = []
	pass_internetfile()
	CONFIG = readConfig(CONFIG_FILE) #type is list
	#date down
	goal_show = setting_show()
	while goal_show != 0:
		rpo = CONFIG[goal_show-1] #type is dict
		#initialize
		goal_show -= 1
		(openwho,opentype) = (rpo["actor"]["display_login"],rpo["type"])
		(openwhat,createdtime) = (rpo["repo"]["name"],rpo["created_at"].replace("T"," ").replace("Z",""))
		
		#type define
		opentype = typecorrect(opentype)
		print(openwho,opentype,openwhat,createdtime)
		saveData.append({"who":openwho,"_type":opentype,"what" : openwhat,"time" : createdtime})
	# date is up.
	saveData.reverse()
	writeConfig("save.txt",saveData)

if __name__ == "__main__":
	main()
