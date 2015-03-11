def freqs(fnm):
	f = open(fnm)
	freq = {}
	for line in f:
		for char in line:
			if char in freq:
				freq[char] += 1
			else:
				freq[char] = 1
	return freq

print freqs("a.txt")
