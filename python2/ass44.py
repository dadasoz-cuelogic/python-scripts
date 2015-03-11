class Parent(object):
	def override(self):
		print "Parent override"
	def implicit(self):
		print "Parent implicit"
	def altered(self):
		print "Parent altered"
class Child(Parent):
	def override(self):
		print "Child Override"
	def altered(self):
		print "Child,Before"
		super(Child,self).altered()
		print "Child,After"
dad=Parent()
son=Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()