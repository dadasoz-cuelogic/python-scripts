print "if you are in a dark room.\n there are two doors will you go through the 1. door or 2 door"

door = raw_input(">")

if door == "1":
	print "there is a bear in the room eating a cake wat you would do"
	print "1. take the cake away"
	print "2. scream out loud"
	op = raw_input(">")
	if op == "1":
		print "he will eat your head"
	elif op == "2":
		print "he will eat your leg"
	else:
		print "%s is a better option"%op

elif door == "2":
	print "you stare into the endless abyss at cthulhus retina"
	print "1. blueberries"
	print "2. yellow jacker"
	print "3. understanding revolver yelling melodies"
	instantly = raw_input(">")
	if instantly == "1" or instantly == "2":
		print "you are saved "
	else:
		print "you are not safe"
else:
	print "you tounble around and fall"


'''
it123@it123:~/Documents/exercise27-39$ python ex31.py
if you are in a dark room.
 there are two doors will you go through the 1. door or 2 door
>1
there is a bear in the room eating a cake wat you would do
1. take the cake away
2. scream out loud
>run
run is a better option
it123@it123:~/Documents/exercise27-39$ 


'''
