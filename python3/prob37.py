#printing Head
myfile = open('head.txt')
head = myfile.readlines()[0:10]
for i in range(10):
	print head[i]