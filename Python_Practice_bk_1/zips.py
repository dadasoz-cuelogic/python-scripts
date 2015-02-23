
def zips(a, b):
	lst = []
	lst = [(a[i],b[i]) for i in range(len(a))]
	print lst



zips([1, 2, 3], ["a", "b", "c"])