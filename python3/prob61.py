from mechanize import Browser
f = Browser()
f.open("http://python.org/")
h = f.response().readlines()
for line in h:
	print line