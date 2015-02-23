def cmm_prd(a):
	lst = []
	z = 1
	for i in a:
		if len(lst) <=0:
			lst.append(i)
		else:
			lst.append(i * lst[len(lst)-1])
	return lst

print cmm_prd([1,2,3,4])