# reversing
def reverse(x):
	a = len(x) / 2
	for i in range(a):
		j = i + 1
		x[i], x[-j]= x[-j], x[i]
	return x
print reverse(reverse([1,2,3,4]))
print reverse([1,2,3,4])