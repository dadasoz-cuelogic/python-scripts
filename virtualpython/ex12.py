"""In this exercise, you will need to 
print an alphabetically sorted list of all functions 
in the re module,which contain the word find."""


import re
list=dir(re)
nlist=[]
[nlist.append(i) for i in list if re.search("find",i)!=None]
print sorted(nlist)
