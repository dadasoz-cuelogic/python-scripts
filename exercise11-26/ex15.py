from sys import argv

filename=argv[1]

print "The content for %r is "%filename

txt=open(filename)

print txt.read()


print "enter another file name"
f2=raw_input()

txt2=open(f2)

print "the %r content is"%f2

print txt2.read()
