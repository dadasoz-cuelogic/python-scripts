def cmm(a):
	lst = []
	for i in a:
		if len(lst) <= 0:
			lst.append(i)
		else:
			z = i + lst[(len(lst)-1)]
			lst.append(z)
	return lst

print cmm([1,2,3,4])