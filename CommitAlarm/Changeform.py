from urllib.request import *
#type format is ~Event, So We change the form
def typecorrect(gittype):
	if gittype[len(gittype)-6] == 'e':
		return gittype.replace("Event","d")
	else:
		return gittype.replace("Event","ed")

# You can see the number you want
def setting_show():
	show = input("How do you see? (please input number) ")
	while show.isdigit() == False:
		print("You put the incorrect answer")
		print("Please input right answer")
		show = input("How do you see? (please input number) ")		
	return int(show)

def printForm(printlist):
	temp = 0
	while temp != len(printlist):
		print(printlist[temp]["who"]+"\'s commit is",printlist[temp]["commit_number"])
		temp += 1