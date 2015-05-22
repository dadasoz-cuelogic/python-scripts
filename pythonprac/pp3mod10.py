'''import zipfile
z = zipfile.ZipFile("temp.zip")
for name in z.namelist():
	print name'''
import os
import zipfile

from sys import argv

with zipfile.ZipFile(argv[1], 'w') as myzip:
	for i in argv[2: ]:
		myzip.write(i)

print " ZIP SUCCESSFULLY CREATED"