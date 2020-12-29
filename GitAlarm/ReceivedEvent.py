from UrlTreat import read_data_from_url
from ReadWrite import readConfig

__all__ = ['received_events','show_received_event']

def received_events(user:str):

    resultList = list()
    received_events_txt = read_data_from_url(f'http://api.github.com/users/{user}/received_events')
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

def show_received_event(receivedList:list):
	print("show received event")
	for events in receivedList:
		if ('Writer' in events) and ('EventType' in events) and ('RepoName' in events) and ('Created' in events):
			print(f"{events['Writer']} {events['EventType']} to {events['RepoName']}")