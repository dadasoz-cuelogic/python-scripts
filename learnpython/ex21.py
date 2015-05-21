def type_check(correct_type):
	def first_func(func):
		def second_func(*args):
			if type(*args) is correct_type:
				return func(*args)
			else:
				print "Bad type"
		return second_func
	return first_func

@type_check(int)
def times2(num):
	return num*2

print times2(2)
times2('Not A Number')

@type_check(str)
def first_letter(word):
	return word[0]

print first_letter('Hello World')
first_letter(['Not', 'A', 'String'])