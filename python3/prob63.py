import os
import sys
import urllib
import re
def urlload(a):
	strurl= a
	new=[]
	response=urllib.urlopen(strurl)
	lines=(response.read()).split()
	for line in lines:
		if line.startswith('href') and 'https://' in line:
			new.append((line))
	print new

urlload("http://python.org/")