def foo(a, b, c, *d):
    return len(list(d))

def bar(a, b, c, **d):
    if d.get("magicnumber") == 7:
    	return True
    else: return False

if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
    print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"


"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex15.py
Good.
Better.
Great.
Awesome!
(learnpython)it123@it123:~/Documents/learnpython$ 
"""