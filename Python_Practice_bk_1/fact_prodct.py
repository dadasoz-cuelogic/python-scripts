def prdct(a):
	fact = 1
	while a > 0:
		fact = fact * a
		a -=1
	return fact

print prdct(4)