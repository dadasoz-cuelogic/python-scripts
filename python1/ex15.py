def foo(a, b, c,*args1):
	return len(args1)

def bar(a, b, c,**args2):
    return args2.get("magicnumber")==7


# test code
if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
    print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"