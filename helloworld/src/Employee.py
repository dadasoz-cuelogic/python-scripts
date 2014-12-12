from person import Person
class employee(Person):
    def __init__(self,name,age,id,loc,desg):
        print('Constructor called')
        self.id = id
        print(self.id)
        self.loc = loc
        print(self.loc)
        self.desg = desg
        print(self.desg)
        super(Person, self).__init__()
        
    def display(self):
         print(' %s    :%s    :   %s     %s    :%s % (self.name, self.age, self.id, self.loc, self.desg))
        
    
        