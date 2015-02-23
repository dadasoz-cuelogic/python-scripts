import os

def dir_tree(path):
	lis = os.listdir(path)
	for i in lis:
		if os.path.isdir("%s/%s"%(path,i)):
			print "---\t %s"%i
			dir_tree("%s/%s"%(path,i))
		else:
			print "--- %s"%i

dir_tree("/home/it123/Documents/demodir")