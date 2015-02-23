
def frequency(word, chk):
	dic = {chk:0}
	for w in word:
		if w == chk:
			dic[chk] += 1
	print dic

frequency("Helloo gudmorning","o")