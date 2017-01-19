from urllib.request import *
def pass_internetfile():
	users = input("What is your username? ")
	passwd = input("password? ")
	auth_handler = HTTPBasicAuthHandler()
	openfile = open("internetfile.txt",'w')
	urlu = "http://api.github.com/users/"+ users + "/received_events"
	auth_handler.add_password(None, urlu, users,passwd )
	opener = build_opener(auth_handler)
	install_opener(opener)
	read = opener.open(urlu).read()
	openfile.write(str(read))
	openfile.close()
