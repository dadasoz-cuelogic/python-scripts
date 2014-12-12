from Employee import employee
 
#from Employee import employee
class manager(employee):
    def __init__(self,name, age, id,loc, desg, department):
        self.department = department
        super(employee,self).__init__(name, age, id, loc, desg)
        
    def display(self):
        print(' %s    :%s    :   %s     %s    :%S    :   %s' % (self.name, self.age, self.id,self.loc,self.desg,self.department))