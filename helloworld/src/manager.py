from Employee import employee
 
#from Employee import employee
class manager(employee):
    'Derived class : Inherits employee'
    def __init__(self,name, age, id, loc, desg, department):
        print('manager Constructor called')
        self.department = department
        print(self.department)
        employee.__init__(self,name, age, id, loc, desg)
        
    def display(self):
        print(' %s    :%s    :   %s     %s    :%s    :   %s' % (self.name, self.age, self.id,self.loc,self.desg,self.department))
        
    def checkDoc(self):
        print('manager.__doc    :    ', manager.__doc__)
        print('manager.__name    :    ', manager.__name__)
        print('manager.__module    :    ', manager.__module__)
        print('manager.__bases    :    ', manager.__bases__)
        print('manager.__dict    :    ', manager.__dict__)
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
        employee.__del__(self)