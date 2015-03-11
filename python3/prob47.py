#implementing Enumerate
def enumerate(x):
	lst = [(x.index(i),i) for i in x]
	return lst

print enumerate(['a','b','c'])
for index, value in enumerate(["a", "b", "c"]):
	print index, value