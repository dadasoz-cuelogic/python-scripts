phonebook = {
	"John" : 9375721772,
	"Jack" : 9342575267,
	"Jill" : 9422369268
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]
#phonebook.pop("Jill")



if "Jake" in phonebook:
	print "Jake is listed in the phonebook."

if "Jill" not in phonebook:
	print "Jill is not listed in the phonebook."




