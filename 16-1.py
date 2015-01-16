from sys import argv
script,filename=argv
print "We're going to erase %r."% filename
print "If you don't want that,hit CTRL_C(^C)."
print "If you do want that,hit RETURN."
raw_input("?")
print "Opening File....."
target=open(filename,'w')
print "Truncating the file....GOodbye"
target.truncate()
print "Now I'm going to ask you for 3 lines ."
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")
print "I'm going to write these to the file."
target.write('%r\n%r\n%r\n' % (line1, line2, line3))
'''target.write("\n")
##target.write(line2)
##target.write("\n")
##target.write(line3)
##target.write("\n")'''
print "And finally,we close it"
target.close()


