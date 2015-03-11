# Finding Duplicates
def dup(x):
	l=[]
	for i in x:
		a = x.index(i) + 1
		if i in x[a:]:
			if i not in l:
				l.append(i)
	return l

print dup([1,2,1,3,2,1,2,5])