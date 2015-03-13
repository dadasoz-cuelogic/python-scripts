import urllib

def url_download(u):
	s = u.split("/")
	#d = {"index":0}
	if ".html" not in s[-1]:	
		urllib.urlretrieve(u,"index.html")
		print "saved it as index.html"
	else:
		urllib.urlretrieve(u,"%s"%s[-1])
		print "saved it as %s"%s[-1]

url_download("http://anandology.com/python-practice-book/modules.html")