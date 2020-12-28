from UrlTreat import pass_internetfile_plus_password
from ReadWrite import readConfig

__all__ = ['received_events','show_received_event']

def received_events():
    resultList = list()
    received_events_txt = pass_internetfile_plus_password()
    received_list = readConfig(received_events_txt) 
    goal_show = 10
    selected_list = received_list[:goal_show]

    for rpo in selected_list:
        
        Writer = rpo["actor"]["display_login"]
        EventType = rpo["type"]
        RepoName = rpo["repo"]["name"]
        Created = rpo["created_at"].replace("T"," ").replace("Z","")
        
        resultList.append({"Writer":Writer,"EventType":EventType,"RepoName" : RepoName,"Created" : Created})
    return resultList
    # # date is up.
    # saveData.reverse()
    # writeConfig("save.txt",saveData)

def show_received_event(receivedList):
	print("show received event")
	for events in receivedList:
		if ('Writer' in events) and ('EventType' in events) and ('RepoName' in events) and ('Created' in events):
			print(f"{events['Writer']} {events['EventType']} to {events['RepoName']}")