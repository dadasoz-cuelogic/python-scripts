from functools import partial

def func(u,v,w,x):
	return u*4 + v*3 + w*2 + x

#t = func(10,2,2,10)
t = partial(func,10,2,2)
#print t(10)
print t(10)