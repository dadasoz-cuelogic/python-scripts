
def extsort(lis):
	for i in range(0,len(lis)):
		for j in range(i+1,len(lis)):
			if lis[i][lis[i].index(".")+1:] > lis[j][lis[j].index(".")+1:]:
				lis[i], lis[j] = lis[j], lis[i]
	print lis

extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])