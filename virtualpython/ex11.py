"""Add "Jake" to the phonebook
 with the phone number 938273443, 
andremove Jill from the phonebook."""

phonebook = {
	"John": 9881124511,
	"Jack": 8421627948,
	"Jill": 9403688612
}

phonebook.update({"Jake":9403688613})
phonebook.pop("Jill")

if "Jake" in phonebook:
	print "Jake is listed in phonebook."

if "Jill" not in phonebook:
	print "Jill not in phonebook"
