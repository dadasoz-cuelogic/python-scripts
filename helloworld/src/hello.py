

def add(x,y):
	print('inside add function')
	return int(x)+int(y)

def sub(x,y):
	print('inside sub function')
	if x > y:
		return int(x)-int(y)
	elif y > x:
		return int(y)-int(x)
	elif x == y:
		return 0;


def mul(x,y):
	print('inside product function')
	return int(x)*int(y)

def div(x,y):
	print('inside div function')
	if int(y) == 0 | int(x)== 0:
		return 0;
	else:
		return int(x)/int(y)
true = 1

while true:
	print('1. ADD ')
	print('2. SUB ')
	print('3. MULTIPLY')
	print('4. DIVISION')
	choice = input('Enter your Choice	:	')
	int1 = input('Enter your number	:	')
	int2 = input('Enter your number	:	')

	if choice == '1':
		print('%s + %s = %s ' % (int1, int2, add(int1,int2)))
	elif choice == '2':
		print('%s - %s = %s ' % (int1, int2, sub(int1,int2)))
	elif choice == '3':
		print('%s * %s = %s ' % (int1, int2, mul(int1,int2)))
	elif choice == '4':
		print('%s / %s = %s ' % (int1, int2, div(int1,int2)))
	else:
		print('Enter valid choice')
	true = input('Do you wish to continue (1/0)	:	')
print("Program terminated!! Thank you")

