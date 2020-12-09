# IT IS not using "github3.py"
#but I know that using "github3.py" is easy. So I append the file, "github3.py" to Directory "USEGITHUB3"

from urllib.request import *
from ReadWrite import *
import datetime
import sys,json

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



def show_commit(user):
	pass

def following_github(user):
	'''
	'''
	list_push = []
	# for following_elem in followingList:
	# 	time = []
	# 	who = following_elem["login"]
	# 	result = pass_internetfile(who,"followers_events.txt","/events")
	# 	for num in range(len(result)):
	# 		date = result[num]["created_at"]
	# 		date = date.split("T")
	# 		now_time = datetime.date.today()
	# 		if date[0] == now_time.isoformat():
	# 			time.append("T".join(date))
	# 	commit_number = len(time)
	# 	who_commit = {"who":who,"commit_number":commit_number}
	# 	list_push.append(who_commit)
	return list_push

#Qt5 GUI


# class show_commit(QWidget):

# 	def __init__(self):
# 		super().__init__()
# 		self.list = following_github()
# 		self.initUI()

# 	def initUI(self):
# 		self.time = 60
# 		self.Label_follow = []
# 		self.setting_commit()
# 		self.setWindowTitle('Show Commit')
# 		self.show()

# 	def setting_commit(self):
# 		self.grid = QGridLayout()
# 		self.grid.setSpacing(10)
# 		list_size = len(self.list)
# 		for list_num in range(list_size):
# 			self.Label_follow.append(QLabel(self.list[list_num]["who"]+"\'s commit is "+str(self.list[list_num]["commit_number"])))
# 			self.grid.addWidget(self.Label_follow[list_num],list_num,0)
# 		self.setLayout(self.grid)
# 		self.setGeometry(list_size*50, list_size*50, 350, 300)

# 	def update_time(self):
# 		self.time -= 1
# 		if self.time < 1:
# 			self.time = 60
# 			[self.Label_follow[i].clear() for i in range(len(self.Label_follow))]
# 			self.setting_commit()

if __name__ == '__main__':
	# users = input("What is your username? ")
	user = 'nOctaveLay'
	print(save_follow(user))
	# print(following_github(user))
	# app = QApplication(sys.argv)
	# ex = show_commit()
	# timer = QTimer()
	# timer.timeout.connect(ex.update_time)
	# timer.start(1000)
	# sys.exit(app.exec_())

