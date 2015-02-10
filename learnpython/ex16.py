import re

def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(your_pattern, email):
            print "You failed to match %s" % (email)
        elif not your_pattern:
            print "Forgot to enter a pattern!"
        else:
            print "Pass"

pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)

"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex16.py
Pass
Pass
Pass
(learnpython)it123@it123:~/Documents/learnpython$ 
"""