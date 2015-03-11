from operator import itemgetter
def valuesort(dic):
	lst = [value for key, value in sorted(dic.items())]
	return lst

print valuesort({'x': 1, 'y': 2, 'a': 3})