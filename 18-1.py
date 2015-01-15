def print_add(*args):
	arg1,arg2=args
	print "arg1:%r,arg2:%r Addition is :%r" %(arg1,arg2,arg1+arg2)
def print_sub(arg1,arg2):
	print "arg1:%r,arg2:%r Subtraction is:%r" %(arg1,arg2,arg1-arg2)
def print_Square(arg1):
	print "arg1:%r Square is:%r" %(arg1,arg1*arg1)
def print_none():
	print "nOthing i got"

print_add(1,4)
print_sub(5,6)
print_Square(7)
print_none()
