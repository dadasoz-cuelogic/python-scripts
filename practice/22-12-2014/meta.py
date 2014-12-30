class CustomMetaclass(type):
    def __init__(cls, name, bases, dct):
        print "Creating class %s using CustomMetaclass" % name
        super(CustomMetaclass, cls).__init__(name, bases, dct)
 
class BaseClass(object):
    print '1'
    __metaclass__ = CustomMetaclass
    print '2'
 
class Subclass1(object):
    print '1'
    __metaclass__ = CustomMetaclass
    print '2'
    
class Subclass2(object):
    print '1'
    __metaclass__ = CustomMetaclass
    print '2'