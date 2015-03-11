#Cummulative Product
def cumm_prod(x):
	l = []
	a = 1
	for i in x:
		if len(l) <= 0:
			a = i
		else:
			a = a * i
		l.append(a)
	return l

print cumm_prod([1,2,3,4])
print cumm_prod([4,3,2,1])