s = "Hey there! what should this string be?"

print "Length of String is %s \n"%len(s[:20])

print "The first occourance of a at %d \n"%s[5:].index("a")

print "a occours %d times\n"%s.count("a")

print "The first five characters are %s\n"%s[:5]

print "The next five characters are %s\n"%s[5:10]

print "The 12th character is %s\n"%s[12]

print "the last five characters are %s\n"%s[-5:]

print "String to uppercase---> %s\n"%s.upper()

print "String to lower---> %s\n"%s.lower()

if s[26:].startswith("str"):
	print "string starts with str Good"

if s.endswith("be?"):
	print "String ends with ome! Good"

print "slipt the three words--> %s"%s[:15].split(" ")