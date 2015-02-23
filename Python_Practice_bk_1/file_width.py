import sys

fname = sys.argv[1]
width = int(sys.argv[2])

f = open(fname)
line = 0
string = f.read()

string2 = string.replace("\n","")



#\for i in range(0,len(string2)):
#	print string2[i]

#for i in range(0,len(f.read())):
#for a in f:
#	if len(a) == 30:
#		print "\n"
#	print a



"""	
for i in f:
	line += 1
	print i.rstrip()
	if line % width == 0:
		print ("\n")

"""