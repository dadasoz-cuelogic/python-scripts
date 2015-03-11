ten="a b c d e f"
print "wait there are not 10 things in that list.Let's fix dat."
stuff=ten.split(' ')
more_stuff=["g","h","i","j","k"]
while len(stuff)!= 10:
	next=more_stuff.pop()
	print "Adding: ",next
	stuff.append(next)
	print "There r %d items now."%len(stuff)
print "There we go: ",stuff
print "Let's do some things with stuff."
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])