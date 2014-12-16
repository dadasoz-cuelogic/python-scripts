
from inheritance import Employee, Chef, Server, Robot

class Customer:
    def __init__(self,name):
        self.name = name
    def order(self,server):
        print(self.name,' orders from  ' ,server)
    
    def pay(self,server):
        print(self.name,' pays for item to ',server)
        
class Oven:
    def bake(self):
        print('oven bakes')
    
    
class PizzaShop:
    def __init__(self):
        #object of pizza shop embedding objects of server and chef
        self.server = Server ('vishal', 10000)  
        self.chef =  Chef('rahul', 4562)
        self.oven = Oven()
        
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
        
if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('arnav')
    

    
    
     