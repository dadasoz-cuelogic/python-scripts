def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
	return open(filename).read().split()

def main(filename):
    dict={}
    frequency = word_frequency(read_words(filename))
    for word,count in frequency.iteritems():
        dict.update({count:word})
    print dict.items()

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    print word_frequency('sagdghsajgffhsfsdfg')