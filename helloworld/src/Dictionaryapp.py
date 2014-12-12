""" Covered topics in almost upto 17th chapter covering collection objects, if else, while
for loops, iterations and functions and function scopes and variable scopes """



def addUser():
	def acceptKey():
		name = input('Enter name: 	')
		return name
	x = acceptKey()
	if x in Dict:
		print('user exists by this name , Please enter other name')
		addUser()
	else:
		dict2 = {x: 0 }
		Dict.update(dict2)
		print ("Value : %s" %  Dict)
		
def depositMoney():
	def check(name):
		if name in Dict.keys():
			return True
		else:
			return False
			
	def getAmount():
		amount = input('Enter Amount to deposit:	')
		if int(amount) > 0:
			return int(amount)
		else:
			print('please enter valid amount greater than zero')
			getAmount()
				
	name = input('Enter Name:	')
	bool = check(name)
	if bool:
		amount = getAmount()
		amount +=  int(Dict[name])
		dict2 = {name: amount }
		Dict.update(dict2)
		print ("Value : %s" %  Dict)
	else:
		print('account doesnt exist . please reenter name:	')
		depositMoney()	

def withdrawMoney():
	def check(name):
		if name in Dict.keys():
			return True
		else:
			return False
			
	def getAmount():
		amount = input('Enter Amount to Withdraw:	')
		if int(amount) > 0:
			return int(amount)
		else:
			print('please enter valid amount greater than zero')
			getAmount()
			
	def	checkBalance(name,x):
		balance = int(Dict[name])
		if	balance > x:
			return True
		else:
			return False
			
	def withdraw(name,amount):
		amt = int(Dict[name])
		amt -= amount
		dict2 = {name: amt }
		Dict.update(dict2)
		print ("Value : %s" %  Dict)
		
				
	name = input('Enter Name:	')
	bool = check(name)
	if bool:
		amount = getAmount()
		check = checkBalance(name,amount) 
		if check:
			withdraw(name, amount)
		else:
			print('Enter amount lower than balance')
			withdrawMoney()
	else:
		print('account doesnt exist . please reenter name:	')
		withdrawMoney()	
		
def printAll():
	for key in Dict:
		print('%s : %s' % (key, Dict[key]))

def chooseOperation(Choice):
	print('inside Choice function')
	if Choice == '1':
		addUser()
	elif Choice == '2':
		depositMoney()
	elif Choice == '3':
		withdrawMoney()
	elif Choice == '4':
		printAll()

		
def getChoice():
	def check(x):
		if int(x) in [1,2,3,4]: 
			return True
		else:
			return False
	choice= input('Enter your choice:	')
	bool = check(choice)
	if bool:
		return choice
	else:
		getChoice()


	
	

true = 1
#list = [1,2,3,4]
Dict = {}

while true:
	print('Welcome')
	print('press 1 to add user')
	print('press 2 to deposit money')
	print('press 3 to withdraw')
	print('press 4 to display all')
	
	
	choice= getChoice()
	chooseOperation(choice)
		
	true = input('Do you wish to continue (1/0)	:	')
	
	
print('Transaction complete, Thank you.')

