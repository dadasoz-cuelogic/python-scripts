def wrd_frequency(words):
	"""Returns frequency of each word given a list of words.
		>>> wrd_frequency(['a', 'b', 'a'])
			{'a': 2, 'b': 1}
	"""
	frequency = {}
	for w in words:
		frequency[w] = frequency.get(w, 0) + 1
	return frequency

print wrd_frequency(['a', 'b', 'a', 'c', 'b'])