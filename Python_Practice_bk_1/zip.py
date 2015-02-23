import zipfile
import sys

def zip_files():

	with zipfile.ZipFile(sys.argv[1],"w") as myzip:
		for i in range(2,len(sys.argv)):
			myzip.write(sys.argv[i])

zip_files()