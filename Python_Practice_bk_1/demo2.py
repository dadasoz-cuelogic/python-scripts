def read_line(fname):
	f = open(fname)
	for i in f:
		yield i

def print_lines(lines):
	c = 0
	for i in lines:
		for a in i:
			if c == 30:
				break
			print a,
			c += 1

a = read_line("abc.txt")
print_lines(a)