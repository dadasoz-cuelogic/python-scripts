import os.path

#get Current working directory
dir= os.getcwd()
print dir

#get Specified directory
from os.path import expanduser
home = expanduser("~/Desktop")

print home

#Save file to directory

#save_path = '../22-12-2014/files'

save_path=home

name_of_file = "test"

completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

file1.write("Test Data")

file1.close()