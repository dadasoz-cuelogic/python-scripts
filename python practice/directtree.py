''''import os
def directtree(path):
	for path, dirs, files in os.walk(path):
  		print path
  		for f in files:
		    print str(f)

directtree('clone')
import os
def printRootStructure(dirname,indent=0):
        for i in range(indent):
            print "   ",
        print dirname
        if os.path.isdir(dirname):
            for files in os.listdir(dirname):
                printRootStructure(files,indent+2)


printRootStructure("python-scripts")'''

import os
def printRootStructure(dirname,indent=0):
    for i in range(indent):
        print "   ",
    print os.path.basename(dirname) # changed
    if os.path.isdir(dirname):
        for files in os.listdir(dirname):
            printRootStructure(os.path.join(dirname,files),indent+1)

printRootStructure("python-scripts")