dict={1:{"name":"dadaso zanzane","email":"dadaso.zanzane@cuelogic.co.in","mobile":"9970420742"},2:{"name":"dadaso zanzane","email":"dadaso.zanzane@cuelogic.co.in","mobile":"9970420742"}}

#Extract the values from dictionary

for row in dict.values():
    print "name=%s, email= %s, mobile=%s" %(row["name"],row["email"],row["mobile"])

#Delete the dictionary with all the data    
#dict.clear()
#dict2={3:{"name":"Nishant Zanzane","email":"nishant@gmail.com","mobile":"9970420742"}}
dict.update({3:{"name":"Nishant Zanzane","email":"nishant@gmail.com","mobile":"9970420742"}})

print(dict)
#Delete given element from dictionary
del dict[3]

print(dict)