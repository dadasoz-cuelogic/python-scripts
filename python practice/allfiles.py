import os
import sys
def directoryfiles(**argv):
	cmd = 'ls '+sys.argv[1]
	return os.system(cmd)


print directoryfiles()