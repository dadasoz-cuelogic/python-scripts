import zipfile
z = zipfile.ZipFile("clone.zip")
for name in z.namelist():
    print name