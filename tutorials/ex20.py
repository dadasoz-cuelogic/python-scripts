def type_check(correct_type):
	def type_checker(old_function):
		def new_function(*args,**kwargs):
			if correct_type == "int":
				if type(args[0]) != int:
					raise TypeError, "Integer Argument Required"
			if correct_type == "str":
				if type(args[0]) != str:
					raise TypeError, "String Argument Required"
			return old_function(*args, **kwargs)
		return new_function
	return type_checker
	
@type_check("int")
def times2(num):
    return num*2

print times2(2)

#Uncomment below line to raise exception
#times2('Not A Number')

@type_check("str")
def first_letter(word):
    return word[0]

print first_letter('Hello World')

#Uncomment below line to raise exception
#first_letter(['Not', 'A', 'String'])