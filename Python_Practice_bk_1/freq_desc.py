def frequency(fname):
	f = open(fname).read().split()
	dic = {}
	for item in f:
		dic.setdefault(item,0)

	for w in f:
		if w in dic.keys():
			dic[w] += 1
	temp = dic
	a = sorted(temp.items(), key=lambda x: x[1])
	#sorted_x = sorted(temp.items(), key=temp.itemgetter(0))
	#print sorted_x
	for i in a:
		print i

frequency("temp.txt")