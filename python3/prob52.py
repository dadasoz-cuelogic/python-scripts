def invertdict(a):
	d=dict((value,key) for key,value in a.iteritems())
	return d

print invertdict({'x': 1, 'y': 2, 'z' : 3})