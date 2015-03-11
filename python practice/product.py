def recursivemultiply(x,n):
	if n==0:
		return 0
	else:
		return x+recursivemultiply(x,n-1)

print recursivemultiply(2,8)