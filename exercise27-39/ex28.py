'''
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> False or False
False
>>> True or False
True
>>> True or False
True
>>> True or not(False)
True
>>> False or not(False)
True
>>> "String" == "String"
True
>>> "String" != "String"
False

>>> 1 and (True or("string" == "string"))
True
>>> 1 and (True or(True and not(False)))
True
>>> 1 and (True or(True and not(True)))
True
>>> 


'''