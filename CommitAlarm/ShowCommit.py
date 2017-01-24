from urllib.request import *
from Changeform import * 
from ReadWrite import *
import datetime

def pass_internetfile(users,textfile,setting):
	openfile = open(textfile,'wb')
	url = "http://api.github.com/users/"+ users + setting
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
	time = []
	#O(n^2), Sorry, I revise the big afterwards .
	for following_elem in followingList:
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
	printForm(list_push)
following_github()