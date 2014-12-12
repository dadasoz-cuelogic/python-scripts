class test:
	name="fgh"
	email="fgh"
	def __init__(self):
		print 'Calling parent constructor'
	def show(self,name,email):
		print 'Name- ',name,' Email-',email
a= test()
a.show("nishant","Test")
a.show("nishant1","Test")
a.show("nishant2","Test")