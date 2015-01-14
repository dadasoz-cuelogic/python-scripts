#variables
cars=100
space_in_car=4
drivers=30
passenger=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_pasenger_per_car=passenger/cars_driven
print "there are",cars,"cars avaialable."
print "there are only",drivers,"drievrs availbale."
print "there will be",cars_not_driven,"empty cars."
print "we can transport",carpool_capacity,"people today."
print "We have",passenger,"people today."
print "We need to put about",average_pasenger_per_car,"in each car."
print "Hey %s there." % "you"