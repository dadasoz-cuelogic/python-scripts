counts = [1,2,3,4,5]
fruits = ['apple','mango','grapes','peach']
mixed = [1,'india',2,'usa',3,'malasia']

print "the numbers are"
for count in counts:
	print count

print "The fruits are"

for fruit in fruits:
	print fruit

print "the countries are"

for i in mixed:
	print i

print mixed.pop(0)
print mixed.pop(4)

print "do you want to add to any lis"
print "1. counts"
print "2. fruits"
print "3. mixed"
a = raw_input(">")

if a == "1":
	temp = raw_input("Enter counts")
	counts.append(temp)
	for i in counts:
		print i
elif a == "2":
	temp = raw_input("Enter fruits")
	fruits.append(temp)
	for i in fruits:
		print i
else:
	temp = raw_input("enter country")
	mixed.append("temp")
	for i in mixed:
		print i


'''
it123@it123:~/Documents/exercise27-39$ 
it123@it123:~/Documents/exercise27-39$ python ex32.py
the numbers are
1
2
3
4
5
The fruits are
apple
mango
grapes
peach
the countries are
1
india
2
usa
3
malasia
1
malasia
do you want to add to any lis
1. counts
2. fruits
3. mixed
>2
Enter fruitsStrawberreys
apple
mango
grapes
peach
Strawberreys
it123@it123:~/Documents/exercise27-39$ 

'''
