import os, time
'''import sys
def directoryfiles(*argv):
	list1=''
	llist=[]
	cmd = 'ls -l '+sys.argv[1]
	return os.system(cmd)

directoryfiles()'''

import time
for files in os.listdir('.'):
	print 'fileName:%s'%(files)+"   "+time.ctime(os.stat(files)[9])