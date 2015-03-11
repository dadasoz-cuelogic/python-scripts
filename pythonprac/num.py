import os
import sys
def extcountfiles(myPath):
	tifCounter=0
	for root, dirs, files in os.walk(myPath):
		for file in files:    
			if file.endswith('.py'):
				tifCounter += 1
	return tifCounter
print extcountfiles("python-scripts")