def enumerate(list):
	cnt=0
	lot=[]
	for i in list:
		lot.append((cnt,i))
		cnt+=1
	return lot

print enumerate([1,2,3,4,5,6,7,8,9])

list=[1,2,3,4,5,6,7,8,9]
for i,item in enumerate(list):
	print (i,item)