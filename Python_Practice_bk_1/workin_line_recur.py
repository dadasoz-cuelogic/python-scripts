"""Write a function to compute the total 
number of lines of code, ignoring empty
 and comment lines, in all python files 
 in the specified directory recursively.  """

 import os

def lis_files(path):
	return os.listdir(path)

def line_count(lis):
	x = len(lis)-1
	for y in range(0,x):
		f = open(lis[y])
		count = 0
		for i in f:
			b = i.lstrip(" ")
			if len(i) == 1 or i[0] == "#" or b[0] == "#":
				pass
			else: count += 1
		print "working line in %s is %s"%(lis[y],count)

lis = lis_files("/home/it123/Documents/Python_Practice_bk")
line_count(lis)