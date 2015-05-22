def read_wrds(file):
	return open(file).read().split()

print read_wrds("a.txt")