import os

def open_dir(path):
	lis = os.listdir(path)
	return lis

def rnge(i):
	while i >= 0:
		i -= 1
		yield i

def file_count_recur(a, lis):
	count = 0
	b = iter(rnge(a))
	for i in range(0,a):
		indx = b.next()
		if ".py" in lis[indx]:
			count += 1

	print count

lis = open_dir("/home/it122/python_demo/python-scripts/python3")
l = len(lis)
file_count_recur(l, lis)