import sys
import time
#print "Kenneth"
#print "\b"
#print "cha"
progress = 0
names = ["Kenneth","Alan","Christensen"]
i=0
while progress < 101:
	sys.stdout.write("Download progress: %d%%\b\b\b\r" % (progress))
	sys.stdout.flush()
	progress+=2.5
	time.sleep(0.5)
	i = (i+1) % 3
