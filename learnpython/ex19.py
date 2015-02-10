import json
def add_employee(salaries_json, name, salary):
	s = json.loads(salaries_json)
	s.update({name:salary})
	return json.dumps(s)

salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]