import datetime
import time
print datetime.datetime.now().strftime("%Y/%B/%d %H:%M:%S %p")


localtime = time.localtime(time.time())
print "Local current time :", localtime

aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop();
#print "B List : ", aList.pop(2);

print aList


list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print "min value element : ", min(list1);
print "min value element : ", min(list2);
print "max value element : ", max(list2);

__test=50
test=60

print __test
print test



class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2