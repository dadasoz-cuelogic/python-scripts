f=open('head.txt')

lis=[]
ind=0
def wrap(a):

    if len(a)<=15:
        lis.append(a)
        return
    else:
        if a[15] == ' ':
            lis.append(a[:15])
            wrap(a[15:])
        else:
            ind=a.rfind(' ',0,14)
            lis.append(a[:ind+1])
            wrap(a[ind+1:])



for x in f:
    if len(x)>15:
        wrap(x)
    else:
        lis.append(x)
for x in lis:
    print x