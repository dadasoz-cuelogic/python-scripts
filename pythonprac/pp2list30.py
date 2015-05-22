#print open('a.csv').read()
"""a, b, c
1, 2, 3
2, 3, 4
3, 4, 5"""

def parse_csv(file):
	f1 = open(file , 'r')
	list1 = [i.rstrip('\n').split(",") for i in f1]
	print list1
parse_csv("a.csv")