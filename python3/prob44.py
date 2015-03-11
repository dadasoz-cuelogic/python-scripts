def square(x):
	return x * x
def map(x,y):
	lst=[x(i) for i in y]
	return lst
print map(square, range(5))