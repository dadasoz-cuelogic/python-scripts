import zipfile
z = zipfile.ZipFile("clone.zip")
for name in z.namelist():
    print
    print "FILE:", name
    print
    print z.read(name)