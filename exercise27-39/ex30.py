a = 10
b = 200
c = 30

if a > b:
	print "a is greater"
elif b > c:
	print "b is greater"
else:
	print "c is greatest"


if (a > b) and (a > c):
	print "a is greatest of all"

elif (b > a) and (b > c):
	print "b is greatest"
elif b > a:						#if first elif is true second does not gets printed
	print "second in elif"

else:
	print "c is greatest"

'''
it123@it123:~/Documents/exercise27-39$ python ex30.py
b is greater
b is greatest
it123@it123:~/Documents/exercise27-39$ 

'''