import os
from os.path import expanduser

home = expanduser("~")
print(home)
home += '/'
parsed_directory = home+'pysc2-replay/data_64/'
replay_files_directory = home+'StarCraftII/Replays'
temporary_save_directory = home+'StarCraftII/temp_save_replays'

for fn in os.listdir(parsed_directory):
	filename_without_suffix = os.path.splitext(fn)[0]
	if os.path.isfile(replay_files_directory+'/'+filename_without_suffix+'.SC2Replay'):
		os.rename(replay_files_directory+'/'+filename_without_suffix+'.SC2Replay',\
			temporary_save_directory+'/'+filename_without_suffix+'.SC2Replay')





