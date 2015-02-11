"""The aim of this exercise is to
 print out the JSON string 
 with key-value pair "Me" : 800 added to it."""

import json

def add_employee(salaries_json, name, salary):
	salar = json.loads(salaries_json)
	salar.update({name:salary})
	return json.dumps(salar)

salaries ='{"Alfred" : 300,"Jane" :400}'
new_salaries=add_employee(salaries, "Me", 30800)
decoded_salaries=json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]
print decoded_salaries["Alfred"]

