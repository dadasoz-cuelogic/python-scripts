import os

def direc(path):
	lis = os.listdir(path)
	for i in lis:
		if os.path.isdir("%s/%s"%(path,i)):
			print "|-- %s"%i
			direc("%s/%s"%(path,i))
		else:
			print "\t |-- %s"%i

direc("/home/it122/python_demo/python-scripts/")