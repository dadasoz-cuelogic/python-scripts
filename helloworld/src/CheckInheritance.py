from manager import manager
from Employee import employee
import  person
import inheritance2 
from inheritance2 import Child
if __name__ == "__main__":
    
    obj1 = manager('vishal', 25, 273913, 'pune', 'SD', "HR")
    obj1.display()
    employee.display(obj1)
    person.Person.display(obj1)
    obj1.checkDoc()
    employee.checkDoc(obj1)
    person.Person.checkDoc(obj1)
    
    
    
    c = Child()          # instance of child
    c.childMethod()      # child calls its method
    c.parentMethod()     # calls parent's method
    c.setAttr(200)       # again call parent's method
    c.getAttr()