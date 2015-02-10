class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

print dir(Vehicle)

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex21.py
['__doc__', '__module__', 'color', 'description', 'kind', 'name', 'value']
(learnpython)it123@it123:~/Documents/learnpython$ 

"""