def my_enumerate(x):
	l = [(x.index(a),a) for a in x]
	return l

print my_enumerate(["a","b","c"])