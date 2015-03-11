#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet      equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet

a = raw_input('enter triplet value:')
b = int(a)
c = [(x,y,z) for x in range(1,b) for y in range(x,b) for z in range(y,b) if x+y==z]
print c