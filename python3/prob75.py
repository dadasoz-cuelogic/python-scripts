import os

def list_dir(path):
	return os.listdir(path)

def numbr(n):
	while n >= 0:
		n -= 1
		yield n

def line_count(b,fname):
	itr = iter(numbr(b))
	for z in range(0,b):
		number = itr.next()
		f = open(fname[number])
		count = 0
		for a in f:
			for b in a:
				if b == "\n":
					count +=1
		print "%s has %s lines"%(fname[number],count+1)



lis = list_dir("/home/it122/python_demo/python-scripts/python3")
a = len(lis)-1
line_count(a, lis)