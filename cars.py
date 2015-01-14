cars=100
spaceincar=4.0
drivers=30
passengers=90
carsnotdriven=cars-drivers
cardriven=drivers
carpool_capacity=cardriven*spaceincar
avgpass=passengers/cardriven

print "there are", cars,"cars available. "
print "there are only",drivers,"drivers available"
print "there will be",carsnotdriven,"enpty cars today"
print "we can transport", carpool_capacity,"people today"
print "we have ",passengers,"to carpool today"
print "we need to put about",avgpass,"in each cars"
print "the total cars",cars

'''

it123@it123:~/Documents/python$ python cars.py
there are 100 cars available. 
there are only 30 drivers available
there will be 70 enpty cars today
we can transport 120.0 people today
we have  90 to carpool today
we need to put about 3 in each cars
the total cars 100
it123@it123:~/Documents/python$ 


'''