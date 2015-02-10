mystring = "Hello"
myfloat = 10.0
myint = 20

if mystring == "Hello":
    print "Mystring -> %s"%mystring

if isinstance(myfloat, float) and myfloat == 10.0:
    print "My Float number is %f"%myfloat

if isinstance(myint, int) and myint == 20:
	print "My int is %d "%myint


""" OUTPUT

(learnpython)it123@it123:~/Documents/learnpython$ python ex2.py
Mystring -> Hello
My Float number is 10.000000
My int is 20 
(learnpython)it123@it123:~/Documents/learnpython$ 

"""