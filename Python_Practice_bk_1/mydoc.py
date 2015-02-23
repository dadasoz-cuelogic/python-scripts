import sys
import os
from inspect import isfunction

a = __import__(sys.argv[1])
print a.__doc__

lis = dir(isfunction(a))
print lis
#lis = [i for i in dir(a) if isfunction(i) == True]
#print lis
