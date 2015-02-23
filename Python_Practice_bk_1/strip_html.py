import urllib

f = urllib.urlopen("http://python.org/")
print f.readline()