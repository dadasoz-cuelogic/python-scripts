from sys import argv
from os.path import exists

script,fn1,fn2=argv

print "your source file is %r and your destination file is %r"%(fn1,fn2)

f1=open(fn1)
f2=open(fn2,"a")
indata=f1.read()

print "writing into the file"

print "the length of file %r is %d"%(fn1,len(indata))
print "does the file exist %r "%exists(fn2)

f2.write(indata)

f1.close()
f2.close()

'''
it123@it123:~/Documents/exercise$ python ex17.py abc.txt xyz.txt
your source file is 'abc.txt' and your destination file is 'xyz.txt'
writing into the file
the length of file 'abc.txt' is 28
does the file exist True 
it123@it123:~/Documents/exercise$ 




'''