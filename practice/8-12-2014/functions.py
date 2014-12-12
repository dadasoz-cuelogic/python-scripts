def outer():
	x = 'old'
	def changer():
		x = 'new'
		return x
	print (changer())

outer()

