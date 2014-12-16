class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def giveRaise(self,percent):
        self.salary = self.salary + (self.salary*percent)
        
    def work(self):
        print(self.name, '    does stuff')
        
    def __repr__(self):
        return "<Employee : name:%s     salary:%s" % (self.name,self.salary)
    
class Chef(Employee):
    def __init__(self, name , salary):
        Employee.__init__(self, name, salary)
        
    def work(self):
        print(self.name, '    makes food')
        
class Server(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self, name, salary)
        
    def work(self):
        print(self.name, '    serves food')
        

class Robot(Chef):
    def __init__(self,name,salary):
        Chef.__init__(self, name, salary)
    def work(self):
        print(self.name, '    Makes Pizza')
        

if __name__ == '__main__':
    
    viz = Robot('vishal',10000)
    print(viz)
    viz.work()
    viz.giveRaise(0.3)
    print(viz)
    
    for x in Employee, Chef, Server, Robot:
        obj = x(x.__name__,10000)
        obj.work()
        