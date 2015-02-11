"""Try to fix the code to 
print out the correct information by changing the string."""

s = "Hey there! what should this string be?"

print "\nLength of s = %d" % len(s)

print "\nThe first occurence of the letter a = %d" % s.index("a")

print "\na occurs %d times " % s.count("a")

print "\nThe first five characters are '%s'" % s[1:5]
print "\nThe next five characters are '%s'" % s[5:1]
print "\nThe twelfth character  is '%s'" % s[12]

print "\nString in lowercase: %s " % s.lower()
print "\nString in uppercase: %s " % s.upper()

if s.startswith("Hey"):
	print "\nString starts with 'Hey'.Good!"

if s.endswith("be?"):
	print "\nString ends with 'be?'!.Good"

print "\nSplit the words of the String: %s" % s.split(" ")
