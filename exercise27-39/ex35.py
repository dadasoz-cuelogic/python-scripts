
def gold_room():
	print "welcome to the gold room"
	how = raw_input("enter how many gold you want")

	if how == "1" or how == "0":
		print "you are not greedy"

	elif how > 50:
		print "you are greedy get out"
		exit(0)


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print "1. take honey"
    print "2. taunt bear and bear dont move"
    print "3. taunt beat and bear move"
    print "4. open door and bear moved"
    choice=raw_input(">")
    bear_moved=False

    if choice == "1":
    	print "dam the bear is gonna eat you now"
    elif choice == "2" and not(bear_moved):
    	print "the bear has moved from door and you can go in"
    elif choice == "3" and bear_moved:
    	print "the bear chewd your leg"
    elif choice == "4" or bear_moved:
    	gold_room()
    else:
    	print "i have no clue what you have typed"

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print "1. flee"
    print "2. head"

    choice=raw_input(">")

    if choice == "1":
    	start()
    if choice == "2":
    	cthulhu_room()

def dead(why):
	print why," good job"
	exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    print "1. left"
    print "2. right"

    choice=raw_input(">")

    if choice == "1":
    	bear_room()
    elif choice == "2":
    	cthulhu_room()
    else:
    	print "you stumble around and fall"

start()