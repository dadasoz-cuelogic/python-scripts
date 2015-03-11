def csvdel(filename,delmin):
	f=open(filename)
	list1=[]
	len1=len(f.readlines())
	f.seek(0)
	while(len1!=0):
		str=f.readline()
		list1.append(str.split(delmin))
		len1-=1
	print list1

csvdel('a.csv',',')