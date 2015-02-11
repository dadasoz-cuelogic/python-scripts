'''Pattern Matching for emails'''


import re
pattern =re.compile(r"\[(on|off)\]")
print re.search(pattern,"Mono:Playback 65 [75%][-16.50db] [on]")
print re.search(pattern,"Nada...:-(")

def test_email(your_pattern):
	pattern = re.compile(your_pattern)
	emails=["john@examples.com","python-list@python.org", "wha.t.`1an?ug{}ly@email.com","deepalib9156@gmail.com","aa--------------@-----m"]
	for email in emails:
		if not re.match(pattern, email):
			print "You failed to match %s" % (email)
		elif not your_pattern:
			print "Forgot to enter a pattern!"
		else:
			print "Pass"

pattern=r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)
