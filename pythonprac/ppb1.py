def dups(lst):
	l = list()
	for i in lst:
		if lst.count(i) >= 2:
			l.append(i)
	print l

mlist =[1, 2, 3, 4, 4, 5, 2]
dups(mlist)