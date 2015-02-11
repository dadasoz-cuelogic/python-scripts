user_pass = (("Sam","Sam999"),
	         ("Jack","Jack999"),
	         ("Steve","Steve999"),
	         ("Jene","Jene999"),
	         ("John","John999"),
	         ("Nick","Nick999"),
	         ("Edwin","Edwin999"))

def new_func(func):
	def inner(*args, **kwargs):
		u = raw_input("Please enter your User name >> ")
		p = raw_input("Please enter your password >> ")
		a = (u,p)
		if a in user_pass:
			return func()
		else:
			print "Sorry!! You need to register first"
			raise Exception ("Sorry!! You need to register first")
	return inner


@new_func
def Check_valid():
	print "You have logged in successfully"

Check_valid()
