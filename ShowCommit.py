# IT IS not using "github3.py"
#but I know that using "github3.py" is easy. So I append the file, "github3.py" to Directory "USEGITHUB3"
import datetime
import configparser
import json
import sys
from urllib.request import *

from ReadWrite import *
from UrlTreat import *
# from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication)
# from PyQt5.QtCore import QTimer

__all__ = ['check_user','update_follow','show_commit','following_commit_num']

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
		url_data = read_data_from_url(f"https://api.github.com/users/{user}/{option}")
		json_data = readConfig(url_data)
		follow_list = []
		if json_data != None: 
			for follow_data in json_data:
					follow_list.append(follow_data['login'])
		return follow_list

def following_commit_num(following_list,time = None):
	list_push = []
	for member in following_list:
		time = []
		event_url_data = read_data_from_url(f"https://api.github.com/users/{member}/events")
		event_json_data = readConfig(event_url_data)
		for event_data in event_json_data:
			date = event_data["created_at"]
			date = date.split("T")
			time = datetime.date.today() if time == None else time
			if date[0] == time.isoformat():
				time.append("T".join(date))
		commit_number = len(time)
		who_commit = {"name":member,"contribution_number":commit_number}
		list_push.append(who_commit)
	return list_push

def show_commit(following_list):
	print("show commit")
	for member in following_list:
		if 'name' in member and 'contribution_number' in member:
			print(member['name'],"-",member['contribution_number'])