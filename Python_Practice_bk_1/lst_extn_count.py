import os

def dir_extn_count():
	lis = os.listdir("/home/it123/Documents/Python_Practice_bk")
	lis2 = [i.split(".") for i in lis ]
	a = [ i[1] for i in lis2 ]
	
	st = set(a)
	dic = {}
	for i in st:
		dic[i] = 0

	for i in a:
		if i in dic:
			dic[i] +=1
	print "total number of files with different extenions are"
	
	for i in dic:
		print i, dic[i]

dir_extn_count()


"""OUTPUT

py 39
zip 3
txt 4
html 4
pyc 1


"""