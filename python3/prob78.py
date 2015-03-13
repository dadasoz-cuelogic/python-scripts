# itertools.izip implementation
def my_izip(l1, l2):
	lis = []
	if len(l1) < len(l2):
		min = len(l1)
	else:
		min = len(l2)
	for i in range(min):
		lis.append((l1[i],l2[i]))
	return lis

print my_izip("abc","xy")