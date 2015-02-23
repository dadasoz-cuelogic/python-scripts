
def frequency(fname, chk):
	dic = {chk:0}
	f = open(fname).read().split()
	print f
	for w in f:
		if w == chk:
			dic[chk] = dic.get(chk,0) + 1
	print dic

frequency("temp.txt","she")