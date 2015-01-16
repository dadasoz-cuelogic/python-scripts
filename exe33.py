i=0
while i< 6:
 print """
 1.ADD 
 2.SUB
 3.MULT
 4.DIVIDE
 PLease enter your choice:
 """
 choice=raw_input(">")
 if choice =="1":
	print "Enter Numbers:"
	a=int(raw_input(">"))
	b=int(raw_input(">"))
	c=a + b
	print "Addition \f is :%d"%(c)
#  	break
 if choice =="2":
	print "Enter Numbers:"
	a=int(raw_input(">"))
	b=int(raw_input(">"))
	c=a-b
 	print "Subtraction is\v :%i"%(c)
 if choice =="3":
	print "Enter Numbers:"
	a=int(raw_input(">"))
	b=int(raw_input(">"))
	c=a*b
	print "Multiplication is:%r \a"%(c)
 if choice =="4":
	print "Enter Numbers:"
	a=int(raw_input(">"))
	b=int(raw_input(">"))
	c=a/b
	print "DIVISION is :%r"%(c)
 if choice>"4":
 	exit(0)
 i=i+1;
print "ThankYou"
