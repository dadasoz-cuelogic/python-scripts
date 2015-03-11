def reversef(filename):
     str=[]
     f=open(filename,'r')
     for lines in f.readlines():
             str.append(lines)
     print str[::-1]

filename= raw_input("Enter File Name:")
reversef(filename)