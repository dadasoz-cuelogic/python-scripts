import re
def make_slug(string):
	if '-' in string:
		strsub=re.sub('-','',string)
		strsub=re.sub(' ','-',strsub)
		print strsub
	else:
		print string.replace(' ','-')

make_slug('hello world')
make_slug('helloworld')
make_slug(" --hello-  world--")