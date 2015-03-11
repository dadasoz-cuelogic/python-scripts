#import os
#import sys
import re
test_input = raw_input('>')
if re.match(r'(\d{3})\D*(\d{3})\D*(\d{4})', test_input):
	print ('That is a valid input')  #That is a valid input  
else:
	print ('This is not a valid input')