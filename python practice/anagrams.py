def anagrams(list):
	anag=[]
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if(len(list[i])==len(list[j])):
				if list[i]is list[j]:
					anag.append(list[i])
	print anag

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])