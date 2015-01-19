'''
#implicit inheritance

class parents(object):
	def implicit(self):
		print "Parent class"

class child(parents):
	pass

a = child()
b = parents()

a.implicit()
b.implicit()



#Explicit override

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
'''

class parent(object):
	def altered(self):
		print "before parents altered"

class child(parent):
	def altered(self):
		print "before parents altered c"
		super(child,self).altered()
		print "after altered"


a = parent()
b = child()

a.altered()
b.altered()