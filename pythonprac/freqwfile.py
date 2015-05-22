def wrd_frequency(words):
	"""Returns frequency of each word given a list of words.
		>>> wrd_frequency(['a', 'b', 'a'])
			{'a': 2, 'b': 1}
	"""
	frequency = {}
	for w in words:
		frequency[w] = frequency.get(w, 0) + 1
	return frequency

#print wrd_frequency(['a', 'b', 'a', 'c', 'b'])

def read_wrds(file):
	return open(file).read().split()

#print read_wrds("a.txt")


def mainfile(file):
	
	frequency = wrd_frequency(read_wrds(file))
	for word, count in frequency.items():
		print word, count
	
	#import sys
if __name__ == '__main__':
	
	print mainfile("a.txt")