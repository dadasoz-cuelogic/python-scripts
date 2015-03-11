#Cummulative sum
def cumm_sum(x):
	l = []
	a = 0
	for i in x:
		if len(l) <= 0:
			a = i
		else:
			a = a + i
		l.append(a)
	return l

print cumm_sum([1,2,3,4])
print cumm_sum([4,3,2,1])