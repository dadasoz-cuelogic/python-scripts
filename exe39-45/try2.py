import try1

try1.apple()

print " --------countrys are--------------- "*2
print try1.country

a = raw_input(" do u wanna enter any country Y/N \n ")

if a == "Y" or a == "y":

	b = raw_input(" Enter country code ")

	c = raw_input( "Enter country Name ")	

	try1.country[ b ] = c

	print try1.country

else:
	exit(0)

print " Temp prev ", try1.temp

try1.temp = 20 

print " try next ", try1.temp