'''Handle all the exceptions!'''


actor={"name": "John Cleese", "rank": "awsome"}

def get_last_name():
	ls=actor["name"].split()
	return ls[-1]

print get_last_name()
print "All exceptions caught!Good Job"
print "The actor's last name is %s " % get_last_name()
