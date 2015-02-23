import itertools

def peep(it):
	lis = [ i for i in range(it)]
	print lis[0], lis

peep(int(raw_input("Enter iter item")))