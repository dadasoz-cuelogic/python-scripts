def type_check(correct_type):
	def new_function(func):
		def wrappper(*args):
			if type(*args) is correct_type:
				return func(*args)
			else:
				print "Bad Type"
		return wrappper
	return new_function

@type_check(int)
def times(num):
	return num*2

@type_check(str)
def first_letter(word):
	return word[0]

print times(2)
times('Not a number')
print times(3)
print first_letter('Hello World')
first_letter(['Not','A','String'])
create a decorator for validations of users:
tuple has user name password
take input
username
password
maintain list of existing user as a list of u,p
functio(u,p)
val;idate using decorator
creating exceptionuser doesnot exists

