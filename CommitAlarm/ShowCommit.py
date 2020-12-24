# IT IS not using "github3.py"
#but I know that using "github3.py" is easy. So I append the file, "github3.py" to Directory "USEGITHUB3"
from urllib.request import *
from ReadWrite import *
import datetime
import sys,json
import threading
import configparser
# from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication)
# from PyQt5.QtCore import QTimer


def pass_internetfile(user:str,option:str):
	'''
	read data in url -> decode utf-8 -> return string.
	'''
	url = f"https://api.github.com/users/{user}/{option}" #need modification.
	opener = urlopen(url).read().decode('utf-8')
	return opener


def check_user(user):
	'''
	Is user github real user?
	if true: return user_name
	else: request user_name
	'''
	while not user:
		print("input again")
		user = input("What is your username? ")
	return user

def update_follow(user:str,option:str = 'following'):
	option_list = ['following','follower']
	try:
		if option not in option_list:
			raise ValueError
	except ValueError as e:
		print(e,":",option,"does not in",option_list)
	else:
		url_data = pass_internetfile(user,option)
		json_data = readConfig(url_data)
		follow_list = []
		if json_data != None: 
			for follow_data in json_data:
					follow_list.append(follow_data['login'])
		return follow_list

def show_commit(following_list):
	print("show commit")
	for member in following_list:
		if 'name' in member and 'commit_number' in member:
			print(member['name'],"-",member['commit_number'])

def following_github(following_list):
	'''
	'''
	list_push = []
	for member in following_list:
		time = []
		event_url_data = pass_internetfile(member,"events")
		event_json_data = readConfig(event_url_data)
		for event_data in event_json_data:
			date = event_data["created_at"]
			date = date.split("T")
			now_time = datetime.date.today()
			if date[0] == now_time.isoformat():
				time.append("T".join(date))
		commit_number = len(time)
		who_commit = {"name":member,"commit_number":commit_number}
		list_push.append(who_commit)
	return list_push



if __name__ == '__main__':
	# config = configparser.ConfigParser()
	# config.read('init.ini')
	# user = config['DEFAULT']['user']
	user = 'nOctaveLay'
	
	follow_list = update_follow(user)
	content = following_github(follow_list)
	show_commit(content)