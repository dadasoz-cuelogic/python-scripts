def unique(a):
	l = []
	for i in a:
		if i not in a[a.index(i)+1:]:
			l.append(i)
	return l

print unique([1,3,5,3,1])
