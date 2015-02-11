
user_pwd = (('Shruti', 'shruti0409'),
			("Deepali", "deepal0102"),
			("Faizan", "faizan308"),
			("Ganesh", "ganesh007"))

def up_validate(user_pwd):
	def first_func(func):
		def second_func(*args):
			t = args
			print t
			if t in user_pwd:
				return func(*args)
			else:
				raise Exception("Invalid username and password")
		return second_func
	return first_func

@up_validate(user_pwd)
def chk_upwd(uname,pwd):
	print "Your username and password is valid, Welcome %s" % uname
	

uname = raw_input("Enter your username: ")
pwd = raw_input("Enter your password: ")
chk_upwd(uname, pwd)
		