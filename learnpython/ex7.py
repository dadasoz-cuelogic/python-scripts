number = 10 * 2
second_number = 0
first_array = []
second_array = range(3)

if number > 15:
    print "1"

if first_array:
    print "2"

if len(second_array[:2]) == 2:
    print "3"

first_array = range(1,3)
if len(first_array) + len(second_array) == 5:
    print "4"

if first_array and first_array[0] == 1:
    print "5"

if not second_number:
    print "6"