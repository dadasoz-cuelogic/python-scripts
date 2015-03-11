import os,sys
def extcountfiles(myPath):
	tpyCounter=0
	for root, dirs, files in os.walk(myPath):
		for file in files:    
			if file.endswith('.py') or file.endswith('.pyc'):
				tpyCounter += 1
	return tpyCounter

typ=extcountfiles('python-scripts')
print 'Count:%d'%typ