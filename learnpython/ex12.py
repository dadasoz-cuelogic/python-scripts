import re

b = []
for a in dir(re):
	if "find" in a:
		b.append(a)

b.sort()
for i in b:
	print i

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex12.py
findall
finditer
(learnpython)it123@it123:~/Documents/learnpython$ 

"""