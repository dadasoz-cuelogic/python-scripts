from sys import argv
script,filename=argv
target=open(filename,'w')
target.truncate()
print "Write three lines..."
line1=raw_input("Line 1: ")
line2=raw_input("Line 2: ")
line3=raw_input("Line 3: ")
print "I'm gng to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()
target=open(filename)
print "Displaying the File: "
print target.read()
