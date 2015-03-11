def zip(list1,list2):
	ziplist=[]
	#for i in list1:
	[ziplist.append((list1[i],list2[i])) for i in range(len(list1))]
	return ziplist

print zip([1,2,3],['a','b','c'])