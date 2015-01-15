def add(a,b):
	print "the addition of %d and %d "%(a,b)
	return a+b

def sub(a,b):
	print "the subtraction of %d and %d "%(a,b)
	return a-b

def div(a,b):

	print "the division of %d and %d "%(a,b)
	return a/b

def mul(a,b):
	print "the multiplication of %d and %d "%(a,b)
	return a*b

print "Lets do some maths"

age=add(30,5)
height=sub(78,4)
weight=div(90,2)
iq=mul(10,2)

print "age=%d height=%d weight=%d iq=%d"%(age,height,weight,iq)
tot=add(age,sub(height,div(weight,mul(iq,2))))

print "that becomes",tot,"can you do by "

'''
it123@it123:~/Documents/exercise$ python ex21.py
Lets do some maths
the addition of 30 and 5 
the subtraction of 78 and 4 
the division of 90 and 2 
the multiplication of 10 and 2 
age=35 height=74 weight=45 iq=20
the multiplication of 20 and 2 
the division of 45 and 40 
the subtraction of 74 and 1 
the addition of 35 and 73 
that becomes 108 can you do by 
it123@it123:~/Documents/exercise$ 

'''