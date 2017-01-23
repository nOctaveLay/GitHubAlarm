from urllib.request import *
from Changeform import * 
from ReadWrite import *
import datetime

def pass_internetfile(users,textfile,setting):
	openfile = open(textfile,'w')
	url = "http://api.github.com/users/"+ users + setting
	opener = urlopen(url).read()
	openfile.write(str(opener))
	openfile.close()
	result = readConfig(textfile)
	return result

def following_github():
	users = input("What is your username? ")
	followingList = pass_internetfile(users,"follower.txt","/following")
	# show_clear(str(followingList))
	goal_show = 0
	list_push = []
	for following_elem in followingList:
		result = pass_internetfile(following_elem["login"],"followers_events.txt","/events")
		print(result)
	# pass_internetfile(followingList[0]["login"],"followers_events.txt","/events")
	# while goal_show != len(followingList):
	# openfile = open("temp.txt","w")
	# who = login_id["login"]
	# Commit = urlopen(url).read()
	# openfile.write(str(Commit))
	# openfile.close()
	# print(type(Commit))
	# print()
	print(goal_show)
	goal_show += 1
		# commit_constant = 0
		# print(len(Commit))
		# while commit_constant != len(Commit):
		# 	Commit_local = Commit[commit_constant]
		# 	commit_constant += 1
		# 	github_type = Commit_local["type"]
		# 	github_time = Commit_local["created_at"]
		# 	print(github_time)
		# 	github_time.split("T")
		# 	now_time = datetime.date.today()
		# 	if github_time[0] == now_time.isoformat():
		# 		list_push.append({"type":github_type,"time":github_time})
		# 	else: break
		# github_commit = CommitUrl["payload"]["commits"]
		# commitR = urlopen(CommitUrl).read()
		# print(commitR)
following_github()