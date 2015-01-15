from sys import argv

script,f1=argv

print "Welcome %r your script is %s"%(f1,script)

print "we are gonna erase all the data if you wanna stop press cntrl+z"

print "if you do want press return"

raw_input("?")

print "opening file %r"%f1
tar=open(f1,"w")

print "turncating file %r"%f1
tar.truncate()

print "now enter 4 lines that you wanna write"

l1=raw_input("line1:")
l2=raw_input("line2:")
l3=raw_input("line3:")
l4=raw_input("line4:")

print "im writing to the file"

tar.write("%s \n %s \n %s \n%s"%(l1,l2,l3,l4))
'''tar.write("\n")
tar.write(l2)
tar.write("\n")
tar.write(l3)
tar.write("\n")
tar.write(l4)
'''
print "the file has been written the new contents are"
