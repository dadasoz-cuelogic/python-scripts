f=open('a.csv')
list=[]
len=len(f.readlines())
f.seek(0)
while(len!=0):
	str=f.readline()
	list.append(str.split(','))
	len-=1
print list