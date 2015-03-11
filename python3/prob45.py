def even(x):
	return x %2 == 0

def filter(x,y):
	lst = [i for i in y if x(i) == True]
	return lst
	
print filter(even, range(10))