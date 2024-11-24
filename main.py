from pathlib import Path
import yaml

# from GitAlarm.ShowCommit import *
# from GitAlarm.ReceivedEvent import *
# from configparser import ConfigParser

if __name__ == '__main__':
	
	with open(Path.joinpath(Path.cwd(),"config/config.yaml"),'r') as f:
		config = yaml.safe_load(f) # yaml.safe_load 와 yaml.load의 차이가 뭐지?
	user = config['default']['name']

	# received_event = received_events(user)
	# show_received_event(received_event)	
