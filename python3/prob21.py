# sum of int and string
def sum(x):
	for i in x:
		result=isinstance(i, int)
		if result == False:
			sum1=""
			break
		else:
			sum1=0
	for i in x:
	    sum1=sum1+i
	print sum1
sum(["hello","world"])
sum([1,2,3])
sum(['aa','bb','cc']) 