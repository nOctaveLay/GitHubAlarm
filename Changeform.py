
def typecorrect(gittype):
	if gittype[len(gittype)-6] == 'e':
		return gittype.replace("Event","d")
	else:
		return gittype.replace("Event","ed")

def setting_show():
	show = input("How do you see? (please input number) ")
	while show.isdigit() == False:
		print("You put the incorrect answer")
		print("Please input right answer")
		show = input("How do you see? (please input number) ")		
	return int(show)