from Employee import employee
 
#from Employee import employee
class manager(employee):
    'Derived class : Inherits employee'
    def __init__(self,name, age, id, loc, desg, department):
        print('manager Constructor called')
        self.department = department
        employee.__init__(self,name, age, id, loc, desg)
        
    def display(self):
        print(' %s    :%s    :   %s     %s    :%s    :   %s' % (self.name, self.age, self.id,self.loc,self.desg,self.department))
        
    def checkDoc(self):
        print('manager.__doc    :    ', manager.__doc__)