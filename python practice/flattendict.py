def flattendict(dictc,result=None):
	flag=0
	if result is None:
		result={}

	for key,value in dictc.items():
		if isinstance(value, dict):
			flag=1
			keystr=key
			print keystr
			flattendict(value,result)
			
		else:
				if flag==1:
					print keystr
					keys=keystr+'.'+key
					result.update({keys:value})
					flag=0
				else:
					result.update({key:value})
	return result

print flattendict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})