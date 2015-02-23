

def unflatten_dict(d):
	item = {}
	item2 = {}
	for i,j in d.items():
		if "." in i:
			splt = i.split(".")
			item2[splt[0]] = {splt[1] : j }
			item.update(item2)
		else:
		    item[i] = j
	return item

print unflatten_dict({'a': 1, 'b.x': 2, 'c': 4})

"""OUTPUT

it123@it123:~/Documents/Python_Practice_bk$ python demo.py
{'a': 1, 'c': 4, 'b': {'x': 2}}
it123@it123:~/Documents/Python_Practice_bk$ 

"""