from sys import argv

script,user = argv

prompt='>'

print "welcome %r your script is %s"%(user,script)

print "i would like to ask you a few questions"

print "do you like programming"
like=raw_input(prompt)

print "where do u live"
live=raw_input(prompt)

print "what kind of computer do you have"
hav=raw_input(prompt)

print """
Alright Mr. %r soo you like %s.
You live in %s. I dont knw where it it.
You have %s computer. """%(user,like,live,hav)


'''
t123@it123:~/Documents/exercise$ python ex14.py Faizan
welcome 'Faizan' your script is ex14.py
i would like to ask you a few questions
do you like programming
>Yes
where do u live
>Pune
what kind of computer do you have
>Intel

Alright Mr. 'Faizan' soo you like Yes.
You live in Pune. I dont knw where it it.
You have Intel computer. 
it123@it123:~/Documents/exercise$ 

'''