import urllib
import os
import sys
import re
def urlload(*args):
	strurl=sys.argv[1]
	f=open('interpreter.txt','w')
	response=urllib.urlopen(strurl)
	responsedata=response.read()
	untag=re.sub('<[^>]*>','',responsedata)
	untag1=re.sub('\s+','',untag)
	f.write(untag1)
	f.close()

urlload()