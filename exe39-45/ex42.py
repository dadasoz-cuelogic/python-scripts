class animal( object ):
	pass

class cat(animal):
	def __init__(self, name):
		self.name = name

class dog(animal):
	def __init__(self, name):
		self.name=name


class person( object ):
	def __init__(self,name):
		self.name=name
		self.pet=None

class employee(person):
	def __init__(self,name,salary):
		self.salary=salary
		super(employee,self).__init__(name)  #retrieving from parent class

class fish(object):
	pass

class salmon(fish):
	pass

class halibut(fish):
	pass

rover = dog(" rover ")
satan = cat(" satan ")
frank = employee(" frank ", 120000)

frank.pet=rover

flipper = fish()

crouse = salmon()

harry = halibut()

print " %s %s "%(frank.name,frank.salary)

'''
 frank  120000
''' 