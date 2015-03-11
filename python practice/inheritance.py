class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'


a = A()
b = B()
print a.f(), a.f()
print b.f(), b.g()