from sys import argv

fname=argv[1]

f1=open(fname)

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def line(a,f):
	print a,f.readline()

print "we will print the whole file"
print_all(f1)

print "now we will go to the first"
rewind(f1)

print "lets print one by one"

cur=1

line(cur,f1)
cur=cur+1
line(cur,f1)
cur=cur+1
line(cur,f1) 

'''
t123@it123:~/Documents/exercise$ python ex20.py xyz.txt
we will print the whole file
hi  
this 
is one line 
edithi  
this 
is one line 
edithi  
this 
is one line 
edit
now we will go to the first
lets print one by one
1 hi  

2 this 

3 is one line 

it123@it123:~/Documents/exercise$ 

'''