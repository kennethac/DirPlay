from subprocess import Popen, PIPE
import os

process = Popen("ls",stdout=PIPE)
stdout, stderr = process.communicate()

files = stdout.split("\n")

path,patherr = (Popen("pwd",stdout=PIPE)).communicate()

for song in files:
#	os.system("afplay "+song)
	location =  path[:-1]+"/"+song
	print location	
	os.system('afplay "'+location+'"')
