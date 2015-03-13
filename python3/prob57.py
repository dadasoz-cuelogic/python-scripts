import os

lis = os.listdir("/home/it122/python_demo/python-scripts/python3")
l = [i.split(".") for i in lis]
l1 = [i[1] for i in l]
s = set(l1)
dic = {}
for i in s:
	dic[i] = 0

for i in l1:
	if i in dic:
		dic[i] += 1

for key,value in dic.items():
	print value,key
