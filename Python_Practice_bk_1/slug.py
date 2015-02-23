def slug(string):
	lis = [ i for i in string if i.isalpha() or i == " " ]
	a = "".join(lis).split(" ")
	lis2 = [i for i in a if i.isalpha() ]
	print "-".join(lis2)



slug(raw_input("Enter the string that you want to slug\n\n"))