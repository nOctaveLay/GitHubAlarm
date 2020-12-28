#to use HTTPBasicAuth Handler,build_opener,install_opener, import 
from getpass import getpass
from urllib.request import HTTPBasicAuthHandler,build_opener,install_opener,urlopen

__all__ = ['pass_internetfile_plus_password','pass_internetfile']

def pass_internetfile_plus_password():
	#receive the user's name & password
	users = input("What is your username? ")
	passwd = getpass("password? ")

	#make HTTPBasicAuthHandler, object => it can add the password. 
	auth_handler = HTTPBasicAuthHandler()

	urlu = f"http://api.github.com/users/{users}/received_events"
	
	# add password in url_u by using users and password
	auth_handler.add_password(None, urlu, users,passwd )
	
	#open the auth_handler.
	opener = build_opener(auth_handler)
	
	# install the opener
	install_opener(opener)
	
	#read the server's data
	read = opener.open(urlu).read()

	#file open, that is written user's received_events
	return read.decode('utf-8')

def pass_internetfile(user:str,option:str):
	'''
	read data in url -> decode utf-8 -> return string.
	'''
	url = f"https://api.github.com/users/{user}/{option}" #need modification.
	opener = urlopen(url).read().decode('utf-8')
	return opener