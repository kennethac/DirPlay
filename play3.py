import sys
from subprocess import Popen, PIPE
import os
import curses
import random
import signal
import time
replay = False
shuffle = False

player = None
playing = True

stdscr = None

def interrupted(signum, frame):
	


if len(sys.argv) > 1:
	args = sys.argv[1:]
	for thing in args:
		if thing == "r" or thing == "R":
			replay = True
		if thing == "s" or thing == "S":
			shuffle = True
	print replay, shuffle
			

process = Popen("ls",stdout=PIPE)
stdout, stderr = process.communicate()

files = stdout.split("\n")

path,patherr = (Popen("pwd",stdout=PIPE)).communicate()

def show_songs(songs, current):
	stdscr.clear()
        for song in range(len(songs)):
                line = songs[song]
                if song == current:   
                        line = "* "+line
                stdscr.addstr(song,0,line)
        stdscr.refresh()
	x = stdscr.getch()
	stdscr.addch(1,2,chr(x))
	stdscr.refresh()
	time.sleep(1)

def playArray(a):
	if shuffle == True:
		random.shuffle(a)
	for song in a:
#		os.system("afplay "+song)
		location =  path[:-1]+"/"+song
		show_songs(a,a.index(song))
		os.system('afplay "'+location+'"')
		player = Popen('afplay "'+location+='"',stdout=PIPE)
		playerOut, playererr = process.communicate()



if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()

	try:
		playArray(files)
		if replay == True:
			while 1:
				playArray(files)
	finally:
		curses.echo()
		curses.nocbreak()
		curses.endwin()
