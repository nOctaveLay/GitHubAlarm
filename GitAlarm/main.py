from ShowCommit import *
from ReceivedEvent import *
from configparser import ConfigParser

if __name__ == '__main__':
	# config = configparser.ConfigParser()
	# config.read('init.ini')
	# user = config['DEFAULT']['user']
	# follow_list = update_follow(user)
	# content = today_following_commit_num(follow_list)
	# show_commit(content)

	config = ConfigParser()
	config.read('config.ini')
	user = config['name']
	received_event = received_events()
	show_received_event(received_event)	
