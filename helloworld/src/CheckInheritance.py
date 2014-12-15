from manager import manager
from Employee import employee
import  person
import inheritance2 
from inheritance2 import Child
if __name__ == "__main__":
    
    obj1 = employee('vishal', 25, 273913, 'pune', 'SD')
    obj1.display()
    person.Person.display(obj1)
    
    
    c = Child()          # instance of child
    c.childMethod()      # child calls its method
    c.parentMethod()     # calls parent's method
    c.setAttr(200)       # again call parent's method
    c.getAttr()