ten_things = ("hi welcome to cuelogic technology pvt lmt pune india")

country = ['india','usa','aus','belgium','russia']

stuff = ten_things.split(' ')

while len(stuff) != 13:
	next_one=country.pop()
	stuff.append(next_one)
	print "there are %d items "%len(stuff)


print "there we go",stuff

print "lets do some more with stuff"

print stuff[1]

print stuff[-1]

print stuff.pop()

print " ".join(stuff)

print "-".join(stuff[3:7])