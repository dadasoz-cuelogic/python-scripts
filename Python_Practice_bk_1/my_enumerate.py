def my_enumerate(lis):
	return [ (i, lis[i]) for i in range(len(lis)) ]
 
print my_enumerate(["a","b","c"])