#Sorting strings according to dere length
def lensort(s):
	s.sort( key=len )
	print s 
lensort (['python', 'perl', 'java', 'c', 'haskell', 'ruby'])