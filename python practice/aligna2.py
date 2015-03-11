def align(filename,width):
		str1='aaaaaaaaaaaaaaaaaaaaaaa'
		print str1.center(width,'*')
		f=open(filename,'r')	
		filecont=f.readline()
		print filecont.center(width,'.')
		
filename= raw_input("Enter File Name:")
wid= int(raw_input("Enter Width:"))
align(filename,wid)
