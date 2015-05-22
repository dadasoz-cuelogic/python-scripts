def enumeratetest(list1):
	newl = []
	for (index,value) in enumerate(list1):
		newl.append((index, value))
		 
	return(newl)

print enumeratetest(list1 = ["a", "b", "c", "d"])