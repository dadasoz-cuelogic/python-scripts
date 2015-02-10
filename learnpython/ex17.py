actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
	try:
		surname = actor["name"].split(" ")
		return surname[1]
	except KeyError:
		print "Sorry!! The key is not present going Out"
		exit(0)

get_last_name()
print "All exceptions caught! Good job!"
print "The actor's last name is %s"%get_last_name()

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex17.py
All exceptions caught! Good job!
The actor's last name is Cleese
(learnpython)it123@it123:~/Documents/learnpython$ python ex17.py
Sorry!! The key is not present going Out
(learnpython)it123@it123:~/Documents/learnpython$ 
"""