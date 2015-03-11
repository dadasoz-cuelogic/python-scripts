def parse(fnm):
	f = open(fnm)
	lst = [i.rstrip('\n').split("!") for i in f]
	print lst

parse("csv.txt")
