from person import Person
class employee(Person):
    'Employee class: Inherits Person and derived in manager'
    def __init__(self,name,age,id,loc,desg):
        print('Employee Constructor called') 
        self.id = id
        print(self.id)
        self.loc = loc
        print(self.loc)
        self.desg = desg
        print(self.desg)
        Person.__init__(self, name, age)
        
    def display(self):
        print('%s    :    %s' % (self.id,self.loc))
        
    def checkDoc(self):
        print('EMPLOYEE.__doc    :    ', employee.__doc__)
        print('Employee.__name    :    ', employee.__name__)
        print('Employee.__module    :    ', employee.__module__)
        print('Employee.__bases    :    ', employee.__bases__)
        print('employee.__dict    :    ', employee.__dict__)
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
        Person.__del__(self)
       
        
    
    
        