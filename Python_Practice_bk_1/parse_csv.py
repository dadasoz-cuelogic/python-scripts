def parse(fname,sep,cmt):
	f = open(fname)
	lst = [ i.rstrip('\n').split(sep) for i in f if cmt != i[0] ]
	print lst

parse("parse_csv.txt","!","#")