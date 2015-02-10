data = ("john","Deo",53.44)

message = "hello {0} {1}. Your current balance is {2}"
print message.format(data[0],data[1],data[2])


"""OUTPUT
(learnpython)it123@it123:~/Documents/learnpython$ python ex5.py
hello john Deo. Your current balance is 53.44
(learnpython)it123@it123:~/Documents/learnpython$ 
"""