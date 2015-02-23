def extn(lst):
	a = []
	for i in lst:
		a.append(i.split("."))

	for i in range(0,len(a)):
		for j in range(i+1, len(a)):
			if a[i][1] > a[j][1]:
				a[i], a[j] = a[j], a[i]


print extn(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])