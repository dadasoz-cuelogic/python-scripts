x = object()
y = object()
x_list = []
y_list = []
big_list = []

x_list = [x for i in range(10)]
y_list = [y for i in range(10)]

big_list = x_list + y_list

print "x list contain %d objects "%len(x_list)
print "y list contain %d objects "%len(y_list)
print "big list contain %d objects "%len(big_list)

if x_list.count(x) == 10 and y_list.count(y) == 10:
	print "\nAlmost there"
if big_list.count(x) == 10 and big_list.count(y) == 10:
	print "Great"

""" OUTPUT

(learnpython)it123@it123:~/Documents/learnpython$ python ex4.py
x list contain 10 objects 
y list contain 10 objects 
big list contain 20 objects 

Almost there
Great
(learnpython)it123@it123:~/Documents/learnpython$
""" 