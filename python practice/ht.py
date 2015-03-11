
def headtail(filename):
	cnt=0
	f=open(filename,'r')
	str=f.readlines()
	print "HEAD"
	print str[:10]
	print """"""""""""""""""""""""""""""""""""""""""""
	print "Tail"
	print str[-10:]
filename= raw_input("Enter File Name:")
headtail(filename)