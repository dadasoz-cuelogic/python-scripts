"""The target of this exercise is to create a string, an integer, 
	and a floating point number.and the integer should be named
	myint and should contain the number 20.The string should be 
	named mystring and should contain the word "hello".The floating
	point number should be named myfloat and should contain the number 10, """
	#change this code
mystring = "hello"
#myfloat = 10.0
myfloat = float(7)
myint = 20

#testing code 
if mystring == "hello":
	print "String: %s" % mystring

if isinstance(myfloat, float) and myfloat == 10.0:
	print "Float: %d" % myfloat

if isinstance(myint, int) and myint == 20:
	print "Integer: %d" % myint