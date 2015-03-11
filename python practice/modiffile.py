import os
import sys
import time
def directoryfiles(*argv):
	for files in os.listdir(sys.argv[1]):
		if files.endswith('.%s'):
			print 'fileName:%s'%(files)+"   "+time.ctime(os.stat(files)[9])

directoryfiles()