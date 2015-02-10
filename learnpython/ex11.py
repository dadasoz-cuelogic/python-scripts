phonebook = dict(zip(("john","jack","jill"),(938477566,938377264,947662781)))
phonebook["Jack"] = 938273443

print "The contents are\n"
for a,b in phonebook.iteritems():
	print a,b

if "Jack" in phonebook:
	print "Jack is listed in the phonebook"

z = raw_input("enter the name you wanna delete >> ")

if z in phonebook:
	del phonebook[z]

print "Checking if deleted succesfully"
if z not in phonebook:
	print "%s is not listed in phonebook\n New phonebbok\n"%z
	for p,q in phonebook.iteritems():
		print p,q

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex11.py
The contents are

john 938477566
jack 938377264
jill 947662781
Jack 938273443
Jack is listed in the phonebook
enter the name you wanna delete >> jill
Checking if deleted succesfully
jill is not listed in phonebook
 New phonebbok

john 938477566
jack 938377264
Jack 938273443
(learnpython)it123@it123:~/Documents/learnpython$ 

"""