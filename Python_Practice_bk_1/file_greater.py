import sys

def open_files(finenames):
	for f in finenames:
		for i in open(f):
			yield i

def read(fname):
	for i in fname:
		print i[40:],
 
a = open_files(["abc.txt","xyz.txt"])
read(a)