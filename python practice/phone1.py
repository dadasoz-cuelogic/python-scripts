import re
flag=0
test_input = raw_input('>')
if len(test_input)>28:
	flag=1
if re.match(r'(\d{3})\D*(\d{3})\D*(\d{4})', test_input) and flag==0:
	print ('That is a valid input')  #That is a valid input  
else:
	print ('This is not a valid input')