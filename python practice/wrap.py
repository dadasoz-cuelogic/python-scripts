import textwrap
def wrap(filename,width):
		f=open(filename,'r')	
		str=f.read()
		list=textwrap.wrap(str,width = int(width) )
		for i in list:
			print i		
		
filename= raw_input("Enter File Name:")
wid= raw_input("Enter Width:")
wrap(filename,wid)