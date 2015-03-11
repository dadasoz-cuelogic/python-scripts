def parse(fnm,s1,c1):
	f = open(fnm)
	lst = [i.rstrip('\n').split(s1) for i in f if c1 != i[0]]
	print lst

parse("csv.txt","!","#")