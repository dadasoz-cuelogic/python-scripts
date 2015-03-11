import glob
import os
import sys
def extcountfiles(myPath):
	tifCounter=0
	txtCounter=0
	tcCounter=0
	tcjava=0
	tcothers=0
	tcsv=0
	for root, dirs, files in os.walk(myPath):
		for file in files:    
			if file.endswith('.py') or file.endswith('.pyc'):
				tifCounter += 1
			elif file.endswith('.txt'):
				txtCounter += 1
			elif file.endswith('.c'):
				tcCounter += 1
			elif file.endswith('.java'):
				tcjava += 1
			elif file.endswith('.csv'):
				tcsv += 1
			else:
				tcothers+=1
	print "Count for Python files: %d"%tifCounter
	print "Count for C files: %d"%tcCounter
	print "Count for Text files: %d"%txtCounter
	print "Count for Java files: %d"%tcjava
	print "Count for Other files: %d"%tcothers
	print "Count for CSV files: %d"%tcsv

extcountfiles("clone")
print '...............docs.................'
extcountfiles("docs")
print '...............python-scripts.................'
extcountfiles("python-scripts")
print '................................'
extcountfiles(".")


'''print "Number of .txt files =", len(glob.glob("*.txt"))
print "Number of .py files =", len(glob.glob("*.py"))
print "Number of .bin files =", len(glob.glob("*.bin"))'''