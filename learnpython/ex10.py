class vehicles(object):
	name = ""
	value = 1000.00
	colour = ""
	kind = "car"

	def description(self):
		desc = "%s is a %s %s worth $%.2f." % (self.name, self.colour, self.kind, self.value)
		return desc

car1 = vehicles()
car1.name = "Fer"
car1.value = 60000
car1.colour ="Red"
car1.kind = "Convertible"

car2 = vehicles()
car2.name = "Jump" 
car2.value = 10000 
car2.colour = "Blue"
car2.kind = "Van"

print car1.description()
print car2.description()

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex10.py
Fer is a Red Convertible worth $60000.00.
Jump is a Blue Van worth $10000.00.
(learnpython)it123@it123:~/Documents/learnpython$ 

"""