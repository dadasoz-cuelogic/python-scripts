from person import Person
class employee(Person):
    'Employee class: Inherits Person and derived in manager'
    def __init__(self,name,age,id,loc,desg):
        print('Constructor called') 
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
       
        
    
    
        