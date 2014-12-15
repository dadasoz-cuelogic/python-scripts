class Person:
    'Person: supermost class of employee and MAnager'
    def __init__(self, name, age):
        print('base class constructor called')
        self.name = name
        print(self.name)
        self.age = age
        print(self.age)
        
    def display(self):
        print('%s    :    %s' % (self.name,self.age))
        
    def checkDoc(self):
        print('person.__doc    :    ', Person.__doc__)
        print('person.__name    :    ', Person.__name__)
        print('person.__module    :    ', Person.__module__)
        print('person.__bases    :    ', Person.__bases__)
        print('Person.__dict    :    ', Person.__dict__)
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")