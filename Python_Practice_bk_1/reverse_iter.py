class reverse_iter:

	def __init__(self, n):
		self.n = n
		self.i = len(n) - 1

#	def __iter__(self):
#		return self

	def next(self):
		if self.i >= 0:
			print self.n[self.i]
			self.i -= 1
		else:
			raise StopIteration

a = reverse_iter([1,2,3,4])
a.next()
a.next()
a.next()
a.next()
a.next()

"""a = reverse_iter([1,2,3,4,5])
while True:
	z = raw_input("input ")
	if z ==1:
		a.next()"""