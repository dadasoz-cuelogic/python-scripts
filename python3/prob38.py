# printing Tail
myfile = open('head.txt')
#head = myfile.readlines()[-10:]
for i in head.readlines():
	if i == sys.argv[2]:
		print i