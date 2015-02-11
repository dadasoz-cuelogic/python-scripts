tuplein=(('abc','ABC'),
		('bcd','234'),
		('cde','345'),
		('def','456'),
		('efg','567'))


def check_validation(tuplein):
	def new_func(func):
		def wrapper(*args):
			#list=args
			tup=args
			print tup
			if tup not in tuplein:
				raise Exception("Invalid UserName and password")
			else:
				return func(*args)
		return wrapper
	return new_func

	
@check_validation(tuplein)
def authenticate(un,ps):
	print('Valid User:%s:)Welcome'%un)

un=raw_input("Enter UserName:")
ps=raw_input("Enter Password:")
authenticate(un,ps)
