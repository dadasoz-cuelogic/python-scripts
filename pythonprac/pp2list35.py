def chr_freqs(lst1):
	freqs = {}
	for line in lst1:
		for char in line:
			if char in freqs:
				freqs[char] += 1
			else:
				freqs[char] = 1

	print freqs

lst1 = open("a.txt", 'r')

print chr_freqs(lst1)

