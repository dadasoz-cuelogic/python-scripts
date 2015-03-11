import re
import os
import sys
import urllib
def urlload(*args):
	strurl=sys.argv[1]
	f=open('untaghtml.txt','w')
	response=urllib.urlopen(strurl)
	responsedata=response.read()
	untag=re.sub('<[^>]*>','',responsedata)
	untag1=re.sub('\s+','',untag)
	f.write(untag1)
	f.close()

urlload()