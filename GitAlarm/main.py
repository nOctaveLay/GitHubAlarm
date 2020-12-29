from ShowCommit import *
from ReceivedEvent import *
from configparser import ConfigParser

if __name__ == '__main__':
	config = ConfigParser()
	config.read('config.ini')
	user = config['Default']['name']
	
	test_mode = config['Default']['mode']
	# follow_list = update_follow(user)
	# content = following_commit_num(follow_list)
	# show_commit(content)

	received_event = received_events(user)
	show_received_event(received_event)	
