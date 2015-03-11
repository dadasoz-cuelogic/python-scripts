p=30
c=40
t=15

if c>p:
	print "Take cars."
elif c<p:
	print "Do Not Take cars."
else:
	print "We Can't decide."

if t>c:
	print "Too many trucks."
elif t<c:
	print "May b Take trucks."
else:
	print "We still can't decide."

if p>t:
	print "Just take trucks."
else:
	print "Stay Home..."