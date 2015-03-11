"""Problem 24: Provide an implementation for zip 
function using list comprehensions."""

def zipfunc(x, y):
	listcomp = [(x[i],y[i]) for i in range(len(x))]
	return listcomp

print zipfunc([1, 2, 3], ["a", "b", "c"])