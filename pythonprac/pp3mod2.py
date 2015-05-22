import os
import sys
def extcount(filenames):
	cnt=0;cnt1=0;cnt2=0
	for (dirnames, dirs, files) in os.walk('.'):
		for filenames in files:
			if filenames.endswith('.txt'):
				cnt += 1
			elif filenames.endswith('.py'):
				cnt1 += 1
			elif filenames.endswith('.csv'):
				cnt2 += 1	
		print "\nTotal number of .txt files are: %d" % cnt
		print "\nTotal number of .py files are: %d" % cnt1
		print "\nTotal number of .csv files are: %d" % cnt2
				
extcount("mypython1\pythonprac")