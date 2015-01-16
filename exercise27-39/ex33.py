num = []

for i in range(10):
	num.append(i)
	i=i+1
	print "numbers now",num
	print "the number at bottom is ",num[i-1]


for i in num:
	print i

'''
it123@it123:~/Documents/exercise27-39$ python ex33.py
numbers now [0]
the number at bottom is  0
numbers now [0, 1]
the number at bottom is  1
numbers now [0, 1, 2]
the number at bottom is  2
numbers now [0, 1, 2, 3]
the number at bottom is  3
numbers now [0, 1, 2, 3, 4]
the number at bottom is  4
numbers now [0, 1, 2, 3, 4, 5]
the number at bottom is  5
numbers now [0, 1, 2, 3, 4, 5, 6]
the number at bottom is  6
numbers now [0, 1, 2, 3, 4, 5, 6, 7]
the number at bottom is  7
numbers now [0, 1, 2, 3, 4, 5, 6, 7, 8]
the number at bottom is  8
numbers now [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
the number at bottom is  9
0
1
2
3
4
5
6
7
8
9
it123@it123:~/Documents/exercise27-39$ 

'''