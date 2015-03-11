def extsort(x):
	a , b = [] , []
	for i in x:
		a.append(i.split('.'))
	for i in range(0,len(a)):
		for j in range(i+1,len(a)):
			if a[i][1] > a[j][1]:
				a[i], a[j] = a[j], a[i]
	for i in a:
		b.append('.'.join(i))

	return b

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])