import collections 
class OrderedClass(type):
     print(3)
     @classmethod
     def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()
        print(4)
     def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        print(result)
        return result

class A(metaclass=OrderedClass):
    print(1)
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

print(2)
print(A.members)
print(6)