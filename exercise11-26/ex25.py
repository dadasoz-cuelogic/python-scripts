def break_word(word):
	res=word.split(' ')
	return res

def sort(word):
	res=sorted(word)
	return res

def first(word):
	a=word.pop(0)
	print a

def last(word):
	a=word.pop(-1)
	print a

def sort_sen(sen):
	words=break_word(sen)
	return sort(words)

def first_last_sentence(sen):
	words=break_word(sen)
	first(words)
	last(words)

def first_and_last_sorted(word):
	words=sort(word)
	first(words)
	last(words)




'''print break_word("ABCD EFGH")
print sort("zyxbca")
first("help")
last("help")
'''