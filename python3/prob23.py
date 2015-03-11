#Factorial
def prod(x):
	p = 1
	for i in x:
		p = p * i
	return p

def fact(a):
	f = range(1,a+1)
	b = prod(f)
	print b

fact(4)