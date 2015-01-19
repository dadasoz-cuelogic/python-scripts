# WE CAN PASS LIST AND DICTIONARYS

class song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics#[ " MY BIrthday Song ",
						#" Please Sing a song for me " ]
		

	def sing(self):
		for i in self.lyrics:
			print i  #self.lyrics[i]

b = [" MY BIrthday Song "," Please Sing a song for me "]

#a = song({" IN ":" India ",
#			"AUS ": " Australia "})

a = song(b)

a.sing()

'''
it123@it123:~/Documents/exe39-45$ python ex40.py 
 India 
 Australia 
it123@it123:~/Documents/exe39-45$ 

'''
