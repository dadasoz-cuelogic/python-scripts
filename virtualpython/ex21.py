'''Edit the function provided by calling partial() 
and replacing the first three variables in func(). 
Then print with the new partial function using only one 
input variable so that the output equals 60.'''

from functools import partial

def func(u,v,w,x):
	return u*4 + v*3 + w*2 +x

def quadrilateral(x,y,z,a,b,c,d):
	return x + y + z + a + b + c + d

result=partial(func,10,2,2)
print result(10)

sumoq=partial(quadrilateral,1,2,3,4,5)
print sumoq(6,7)
