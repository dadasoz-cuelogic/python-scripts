import sys

def splitfile():
	f=open(sys.argv[1])
	length=len(f.read())
	cnt=1
	splitfact=int(length/int(sys.argv[2]))
	for i in range(int(sys.argv[2])):
		f1=open((sys.argv[1]+str(cnt)+'.txt'),'w')
		cnt=cnt+1
		f.seek(splitfact*i)
		f1.write(f.read(splitfact))
		f1.close()
	return 0


s=splitfile()
print s