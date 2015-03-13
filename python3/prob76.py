def peep(it):
	lis = [ i for i in range(it)]
	return lis[0], lis

x, l = peep(int(raw_input("Enter iter item>>")))
print x,l