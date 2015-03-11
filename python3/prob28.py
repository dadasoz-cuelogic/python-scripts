#Finding Unique
def uni(x):
	l=[]
	for i in x:
		a = x.index(i) + 1
		if i not in x[a:]:
			l.append(i)
	return l

print uni([1,2,1,3,2,5])