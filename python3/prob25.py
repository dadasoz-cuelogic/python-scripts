#min and max
def min(a):
	minimum=a[0]
	for i in a:
		if i < minimum:
			minimum = i
	return minimum

def max(a):
	maximum=a[0]
	for i in a:
		if i > maximum:
			maximum = i
	return maximum

print min([3,1,4,7])
print max([3,1,4,7])
print min(["s","a","c","z"])
print max(["s","a","c","z"])