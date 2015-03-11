def invertdictn(dict1):
	dict2 = {}
	for key, value in dict1.iteritems():
		dict2.update({value:key})	#like in list we use append method
	print dict2.items()


dict1 = {'x': 1, 'y': 2, 'z': 3}
invertdictn(dict1)