def addOne(myFunc):
    def addOneInside(*args,**kwargs):
        return myFunc(*args,**kwargs)+" World"
    return addOneInside

@addOne
def oldFun(x):
    return x

print oldFun("Hello")