#to use HTTPBasicAuth Handler,build_opener,install_opener, import 
from urllib.request import *
def pass_internetfile():
	#receive the user's name & password
	users = input("What is your username? ")
	passwd = input("password? ")

	#make HTTPBasicAuthHandler, object => it can add the password. 
	auth_handler = HTTPBasicAuthHandler()
	
	#file open, that is written user's received_events
	openfile = open("internetfile.txt",'w')
	urlu = "http://api.github.com/users/"+ users + "/received_events"
	
	# add password in url_u by using users and password
	auth_handler.add_password(None, urlu, users,passwd )
	
	#open the auth_handler.
	opener = build_opener(auth_handler)
	
	# install the opener
	install_opener(opener)
	
	#read the server's data
	read = opener.open(urlu).read()
	openfile.write(str(read))
	openfile.close()

