import os
import sys
import urllib
def urlload(*args):
	strurl=sys.argv[1]
	save=''
	list=strurl.split('/')	
	if strurl.endswith('/'):
		save='index.html'
	else:
		save=list[-1]
	f=open(save,'w')
	response=urllib.urlopen(strurl)
	f.write(response.read())
	f.close()

urlload()