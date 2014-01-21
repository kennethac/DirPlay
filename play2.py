import re
import sys
from subprocess import Popen, PIPE
import os
import curses
import random

replay = False
shuffle = False


if len(sys.argv) > 1:
	args = sys.argv[1:]
	for thing in args:
		if thing == "r" or thing == "R":
			replay = True
		if thing == "s" or thing == "S":
			shuffle = True
	print replay, shuffle
			

process = Popen("ls -R",shell=True,stdout=PIPE)
stdout, stderr = process.communicate()
files = []
dirs = stdout.split("./")
for i in range(len(dirs)):
	dirs[i] = dirs[i].strip()
if len(dirs) > 1:
	for i in range(len(dirs)):
		hold = dirs[i].split(":")
		if len(hold) > 1:
			pts = hold[1].split("\n")
			for thing in pts:
				files.append(hold[0]+"/"+thing)
		else:
			for thing in hold[0].split("\n"):
				files.append(thing)
else: 	
	files = stdout.split("\n")


path,patherr = (Popen("pwd",stdout=PIPE)).communicate()

def show_songs(songs, current):
	height,width = stdscr.getmaxyx()
	maxLength = width-3
	space = height - 3
	stdscr.clear()
	low = current-(space/2)-1
	if low<(space/2):
		low = 0
	high = low + space	
    
	stdscr.addstr(0,0,"DirPlay Playlist")
	stdscr.addstr(1,0," " + ("-"*(width-2)) + " ")
	for song in range(len(songs))[low:high]:
                line = songs[song]
                if song == current:   
                        line = "* "+line
                stdscr.addstr(song-low+3,0,line[:maxLength])
        stdscr.refresh()

def playArray(a):
	if shuffle == True:
		random.shuffle(a)
	for song in a:
#		os.system("afplay "+song)
		location =  path[:-1]+"/"+song
		location = location.replace('"','\\"')
		show_songs(a,a.index(song))
		x = os.system('afplay "'+location+'"')

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
