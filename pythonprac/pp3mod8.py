from string import find
from urllib import urlopen
import os
import sys

def findlinks(*args):
	
	strlink = sys.argv[1]
	n = 1 
	s = []
	f = urlopen(strlink).read()
	while n > 0:
		n = f.find('"http://')
		f = f[n + 1:]
		n = f.find('"')
		
		s.append(f[:n])
		f = f[n:]
		n = f.find('"http://')
	print s

findlinks()