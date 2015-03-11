count=[1,2,3,4,5]
change=[1,'pennies',2,'dimes',3,'quarters']

for no in count:
	print "count is: %d"%no

for i in change:
	print "I got %r" %i

elements=[]

print "Creating new list:"
for i in range(0,6):
	print "Adding %d to the list."%i
	elements.append(i)

print "List becomes:"
for i in elements:
	print i