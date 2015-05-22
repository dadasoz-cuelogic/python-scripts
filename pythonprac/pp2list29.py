def funcarray(x, y, z):
	'''if x and y >= 2:
		print "sorry its a 2 dimenstional array"
		exit(0)'''

	l1,l2 = [],[]
	for i in range(2):
		l1.append("None")
		l2.append("None")

	list1 = []
	list1.append(l1)
	list1.append(l2)
	list1[x][y] = z
	print list1

funcarray(1,1,5)