def triplet(no):
	list=[]
	for i in range(no):
		for j in range(no):
			for k in range(no):
				if(i+j==k) and [j,i,k] not in list:
					list.append([i,j,k])
	return list

print triplet(5)
