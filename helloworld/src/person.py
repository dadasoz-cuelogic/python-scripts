class Person:
    def __init__(self, name, age):
        print('base class constructor called')
        self.name = name
        self.age = age
        
    def display(self):
        print('%s    :    %s' % (self.name,self.age))