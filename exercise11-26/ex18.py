def first(*p):
	z , s = p
	x=p[0]
	y=p[1]
	print "first %r %r "%(z,s)
	print "other first %r %r"%(x,y)

def first_two(a,b):
	print " %r %r"%(a,b)

def one(a):
	print " %r"%a

def none():
	print "none printed"


first("Faizan","Shaikh")
first_two("Faizan","Shaikh")
one("Faizan")
none()

'''
it123@it123:~/Documents/exercise$ python ex18.py
first 'Faizan' 'Shaikh' 
other first 'Faizan' 'Shaikh'
 'Faizan' 'Shaikh'
 'Faizan'
none printed
it123@it123:~/Documents/exercise$ 




'''