def my_izip(l1, l2):
	lis = []
	for i in range(len(l1)):
		lis.append((l1[i],l2[i]))
	return lis

print my_izip(["a", "b", "c"], [1, 2, 3])