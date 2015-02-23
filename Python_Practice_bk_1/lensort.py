def lensort(lst):
	for i in range(0,len(lst)):
		for j in range(i+1, len(lst)):
			if len(lst[i]) > len(lst[j]):
				lst[i], lst[j] = lst[j], lst[i]
	return lst

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
