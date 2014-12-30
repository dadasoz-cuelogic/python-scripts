#dict={1:{"name":"dadaso zanzane","email":"dadaso.zanzane@cuelogic.co.in","mobile":"9970420742"},2:{"name":"dadaso zanzane","email":"dadaso.zanzane@cuelogic.co.in","mobile":"9970420742"}}

#Extract the values from dictionary

#for row in dict.values():
   # print "name=%s, email= %s, mobile=%s" %(row["name"],row["email"],row["mobile"])

#Delete the dictionary with all the data    
#dict.clear()
#dict2={3:{"name":"Nishant Zanzane","email":"nishant@gmail.com","mobile":"9970420742"}}
#dict.update({3:{"name":"Nishant Zanzane","email":"nishant@gmail.com","mobile":"9970420742"}})

#print(dict)
#Delete given element from dictionary
#del dict[3]

#print(dict)


dict1={1:{"name":"dadaso"}}
dict2={2:{"name":"vishal"}}
dict3={2:{"name":"nishant"}}
dict1.update(dict2)

#print 'vishal' in dict1.itervalues()



#print {k: v for k, v in dict1.items() if v['name'] == 'vishafl'}

def findDict(dictn,dict1):
    key= dict1.keys()
    dict1= dict1.get(key[0])
    for data in dictn.values():
        if(dict1["name"]==data["name"]):
            return True
    return False

        

print findDict(dict1, dict3)

#print len(dict1)
#print dict1