import os

def file_detail(path):
	lis = os.listdir(path)
	print "File Name |\t\t File Size    |\t\t File MOdification Time"
	for i in lis:
		lis2 = os.stat("%s/%s"%(path,i))
		print "%s \t\t%s \t\t%s"%(i,lis2[6],lis2[8])

file_detail("/home/it123/Documents/Python_Practice_bk")