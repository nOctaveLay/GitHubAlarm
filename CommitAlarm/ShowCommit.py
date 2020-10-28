# IT IS not using "github3.py"
#but I know that using "github3.py" is easy. So I append the file, "github3.py" to Directory "USEGITHUB3"

from urllib.request import *
from ReadWrite import *
import datetime
import sys,json
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication)
from PyQt5.QtCore import QTimer

def pass_internetfile(users:str,textfile:str,setting:str):
	url = f"https://api.github.com/users/{users}{setting}"
	opener = urlopen(url).read()
	
	with open(textfile,'wb') as f:
		openfile.write(opener)
	
	result = readConfig(textfile)
	return result

def following_github():
	users = input("What is your username? ")
	users = users.strip()
	while not users:
		print("input again")
		users = input("What is your username? ")
	followingList = pass_internetfile(users,"follower.txt","/following")
	# show_clear(str(followingList))
	goal_show = 0
	list_push = []
	#O(n^2), Sorry, I revise the big afterwards .
	for following_elem in followingList:
		time = []
		who = following_elem["login"]
		result = pass_internetfile(who,"followers_events.txt","/events")
		for num in range(len(result)):
			date = result[num]["created_at"]
			date = date.split("T")
			now_time = datetime.date.today()
			if date[0] == now_time.isoformat():
				time.append("T".join(date))
		commit_number = len(time)
		who_commit = {"who":who,"commit_number":commit_number}
		list_push.append(who_commit)
	return list_push

#Qt5 GUI
class show_commit(QWidget):
	
	def __init__(self):
		super().__init__()
		self.list = following_github()
		self.initUI()
		
	def initUI(self):
		self.time = 60
		self.Label_follow = []
		self.setting_commit()
		self.setWindowTitle('Show Commit')	
		self.show()
	
	def setting_commit(self):
		self.grid = QGridLayout()
		self.grid.setSpacing(10)
		list_size = len(self.list)
		for list_num in range(list_size):
			self.Label_follow.append(QLabel(self.list[list_num]["who"]+"\'s commit is "+str(self.list[list_num]["commit_number"])))
			self.grid.addWidget(self.Label_follow[list_num],list_num,0)
		self.setLayout(self.grid) 
		self.setGeometry(list_size*50, list_size*50, 350, 300)
		
	def update_time(self):
		self.time -= 1
		if self.time < 1:
			self.time = 60
			[self.Label_follow[i].clear() for i in range(len(self.Label_follow))]
			self.setting_commit()

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = show_commit()
	timer = QTimer()
	timer.timeout.connect(ex.update_time)
	timer.start(1000)
	sys.exit(app.exec_())

