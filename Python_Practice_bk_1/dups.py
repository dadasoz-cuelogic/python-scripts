def duplicate(a):
	l = []
	for i in a:
		if i in a[a.index(i)+1:]:
			l.append(i)
	return l

print duplicate([1,4,7,9,4,1])
