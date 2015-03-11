f=open('head.txt')

lis=[]
def wrap(a):

    if len(a)<=15:
        lis.append(a)
        return
    else:
        lis.append(a[:15])
        wrap(a[15:])

for x in f:
    if len(x)>15:
        wrap(x)
    else:
        lis.append(x)
for x in lis:
    print x