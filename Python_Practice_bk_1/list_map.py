"""def square(x): 
	return x * x

print map(square, range(5))
"""

print [i for i in map(lambda x: x*x,range(5))]