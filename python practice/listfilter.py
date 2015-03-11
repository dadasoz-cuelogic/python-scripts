def filter(func,list):
	return func(list)

def funceven(list):
	nlist=[]
	for i in list:
		if i%2==0:
			nlist.append(i)
	return nlist

print [filter(funceven,range(10))]