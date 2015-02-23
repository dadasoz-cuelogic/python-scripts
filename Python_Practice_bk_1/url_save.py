import urllib

def url_save(url):
	splt = url.split("/")
	dic = {"index":0}
	if ".html" not in splt[-1]:	
		urllib.urlretrieve(url,"index.html")
		print "saved it as index.html"
	else:
		urllib.urlretrieve(url,"%s"%splt[-1])
		print "saved it as %s"%splt[-1]

url_save("http://anandology.com/python-practice-book/iterators.html")