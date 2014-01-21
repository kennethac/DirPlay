DirPlay
Copyright 2014 Kenneth Christensen
----------------------------------

	DirPlay is a commandline audio player, designed to fill the gap 
between afplay and iTunes. Navigate to the directory which contains the 
music you want to play, run DirPlay, and the program will recursively 
search the directory structure and call afplay on every file. While 
playing, it displays a list of the files, although at the moment it 
offers no way to control the order or repeat songs.

	Pressing Control-C will cause the afplay process to quit, which 
is equivilant to skipping a song. In order to quit DirPlay, you must use 
Control-Z to suspend the process, then run "killall afplay && killall 
DirPlay" in order to close it.

	DirPlay accepts the following commandline arguements:

		's': Shuffle the playlist before playing. When used in 
			conjunction with 'r', the songs will be shuffled 
			on each repeat.

		'r': Repeat the playlist indefinitely.

		'h': Help menu pending.
	
	DirPlay was originally conceived to circumvent the need to be 
logged in to listen to music. To this end, running DirPlay in a screen 
session, then using "Control-A D" to suspend the session will allow you 
to log out. As usual, using 'screen -r' will resume your screen session.
