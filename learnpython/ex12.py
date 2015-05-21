import re 

func_list = []
"""for i in dir(re):
	if "find" in i:
		func_list.append(i) """

l = dir(re)
[func_list.append(i) for i in l if re.search("find" , i) != None]

print sorted(func_list)
