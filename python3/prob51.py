#Mutate Example
import string
def mutate(seq):
	lst = {}
	for x in xrange(len(seq)):
		prefix = seq[:x]
		suffix = seq[x+1:]
		lst.update([(prefix+base+suffix,1) for base in string.ascii_lowercase])
	return lst
words = mutate('hello')
print 'cello' in words
print 'helol' in words
