def arry(a,b,c):
	if a and b >= 2:
		print "sorry its a 2 dimenstional array"
		exit(0)

	l1,l2 = [],[]
	for i in range(2):
		l1.append("None")
		l2.append("None")

	lst = []
	lst.append(l1)
	lst.append(l2)
	lst[a][b] = c
	print lst

	#print lis

arry(1,1,5)