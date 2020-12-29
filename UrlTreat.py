#to use HTTPBasicAuth Handler,build_opener,install_opener, import 
from getpass import getpass
from urllib.request import HTTPBasicAuthHandler,build_opener,install_opener,urlopen

__all__ = ['pass_internetfile_plus_password','read_data_from_url']

def pass_internetfile_plus_password(url,users,password):
	#receive the user's name & password
	# users = input("What is your username? ")
	# passwd = getpass("password? ")

	#make HTTPBasicAuthHandler, object => it can add the password. 
	auth_handler = HTTPBasicAuthHandler()

	# add password in url_u by using users and password
	auth_handler.add_password(None, url, users,password )
	
	#open the auth_handler.
	opener = build_opener(auth_handler)
	
	# install the opener
	install_opener(opener)
	
	#read the server's data
	read = opener.open(url).read().decode('utf-8')

	#file open, that is written user's received_events
	return read

def read_data_from_url(url):
	'''
	read data in url -> decode utf-8 -> return string.
	'''
	opener = urlopen(url).read().decode('utf-8')
	return opener