while True:
	reply=raw_input('Enter Text:')
	if reply=="stop":break
	try:
		num=int(reply)
	except:
		print('Bad!'*8)
	else:
		print(num ** 2)
print('Bye')