people = 30
cars = 30
trucks = 30


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
elif cars==people:
    print "We can't decide."
else:
	print "Nothn"
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
elif trucks==cars:
    print "We still can't decide."
else:
	print "Nothing"
if people > trucks:
    print "Alright, let's just take the trucks."
elif people==trucks:
    print "Fine, let's stay home then."
else:
	print"nothoin2"