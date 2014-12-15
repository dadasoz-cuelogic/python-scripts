from person import Person
class employee(Person):
    def __init__(self,name,age,id,loc,desg):
        print('Constructor called')
        super(Person,self).__init__()
        self.id = id
        print(self.id)
        self.loc = loc
        print(self.loc)
        self.desg = desg
        print(self.desg)
       
        
    
    
        