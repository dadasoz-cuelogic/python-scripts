states = { 
	'Oregon':'OR', 
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI' }

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonvilla'
}

print "add some more cities"

cities['NY'] = " New York "
cities['OR'] = " Portland "

print "-"*10
print "New  york state has city= ",cities['NY']
print "OR state has =",cities['OR']

print "states--"*5
print "Michigan state is ",states['Michigan']
print " Florida state is ",states['Florida']

print "some states and cities--"*2
print " Michigan has",cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print "county and state-----"*2
for a,b in states.items():
	print " %s has %s "%(a,b)

print " print all--- "*3

for a,b in states.items():
	print " %s has %s and %s "%(a,b,cities[b])

n=raw_input("enter state you wanna get")

print states.get(n)

c=raw_input("enter city")

print cities.get(c," Does not Exist ")

'''
it123@it123:~/Documents/exercise27-39$ python ex39.py
add some more cities
----------
New  york state has city=   New York 
OR state has =  Portland 
states--states--states--states--states--
Michigan state is  MI
 Florida state is  FL
some states and cities--some states and cities--
 Michigan has Detroit
Florida has:  Jacksonvilla
county and state-----county and state-----
 California has CA 
 Michigan has MI 
 New York has NY 
 Florida has FL 
 Oregon has OR 
 print all---  print all---  print all--- 
 California has CA and San Francisco 
 Michigan has MI and Detroit 
 New York has NY and  New York  
 Florida has FL and Jacksonvilla 
 Oregon has OR and  Portland  
enter state you wanna getOregon
OR
enter cityMI
Detroit
it123@it123:~/Documents/exercise27-39$ 
'''