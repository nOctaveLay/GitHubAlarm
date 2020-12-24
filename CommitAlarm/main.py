from ShowCommit import *

if __name__ == '__main__':
	# config = configparser.ConfigParser()
	# config.read('init.ini')
	# user = config['DEFAULT']['user']
	user = 'nOctaveLay'
	
	follow_list = update_follow(user)
	content = today_following_commit_num(follow_list)
	show_commit(content)