from urllib.request import *
from Changeform import * 
from ReadWrite import *
import datetime
def pass_internetfile():
	users = input("What is your username? ")
	openfile = open("follower.txt",'w')
	url = "http://api.github.com/users/"+ users + "/following"
	opener = urlopen(url).read()
	openfile.write(str(opener))
	openfile.close()

def events(who):
	# url = "http://api.github.com/users/" + who + "/events"
	# Commit = urlopen(url).read()
	# show_clear(str(Commit))
	list_con = readConfig("clear")
def following_github():
	# pass_internetfile()
	followingList = readConfig("follower.txt")
	# show_clear(str(followingList))
	goal_show = 0
	list_push = []
	events(followingList[0]["login"])
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