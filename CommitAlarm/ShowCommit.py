# IT IS not using "github3.py"
#but I know that using "github3.py" is easy. So I append the file, "github3.py" to Directory "USEGITHUB3"

from urllib.request import *
from ReadWrite import *
import datetime
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication)

def pass_internetfile(users,textfile,setting):
	openfile = open(textfile,'wb')
	url = "https://api.github.com/users/"+ users + setting
	opener = urlopen(url).read()
	openfile.write(opener)
	openfile.close()
	result = readConfig(textfile)
	return result

def following_github():
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
		grid = QGridLayout()
		grid.setSpacing(10)
		list_size = len(self.list)
		for listelem in range(list_size):
			followerL = QLabel(self.list[listelem]["who"]+"\'s commit is "+str(self.list[listelem]["commit_number"]))
			grid.addWidget(followerL,listelem,0)

		self.setLayout(grid) 
		self.setGeometry(list_size*50, list_size*50, 350, 300)
		self.setWindowTitle('Show Commit')	
		self.show()
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = show_commit()
	sys.exit(app.exec_())

