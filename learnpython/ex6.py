s = "Hey there! what should this string be?"

#length should be 20
print "Length of the s = %d" % len(s)

#First occurence of "a" should be at index 8
print "The first occurence of the letter a = %d" % s.index("a")

#Number of a's should be 2
print "a occurs %d times" % s.count("a")

#Slicing the string into bits
print "The first five characters are '%s'" % s[:5] #Start to 5

#convert everything to uppercase
print "String in uppercase: %s" % s.upper()

#convert everything to lowercase
print "String in lowercase: %s" % s.lower()

#Check how string starts
if s.startswith("Str"):
	print "String starts with 'Str'.Good!!"

if s.endswith("ome!"):
	print "String ends with 'ome!'.Good!!"

#Split the string into three separate strings,
#each containing only a word
print "Split the words of the string: %s" % s.split(" ")
