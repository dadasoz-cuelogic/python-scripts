def triplet(n):
	lst = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x + y == z]
	return lst

print triplet(5)