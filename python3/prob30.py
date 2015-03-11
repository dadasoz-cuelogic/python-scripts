def group(a,size):
	lst, lst1= [], []
	for i in a:
		if len(lst) < size:
		    lst.append(i)
		else:
			lst1.append(lst)
			lst = []
			lst.append(i)
	lst1.append(lst)
	return lst1
print group([1,2,3,4,5,6,7,8,9],3)	
print group([1,2,3,4,5,6,7,8,9],4)