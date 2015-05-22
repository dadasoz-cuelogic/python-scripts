import os

def filesindirect():
	cmd = 'cd .'
	os.system(cmd)
	cmd = 'ls'
	return os.system(cmd)

print filesindirect()