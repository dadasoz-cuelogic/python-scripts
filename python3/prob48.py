def array(a,b):
	lst = [[None for i in range(b)] for j in range(a)]
	return lst
a = array(2,3)
print a
a[0][1] = 5
a[1][2] = 10
print a