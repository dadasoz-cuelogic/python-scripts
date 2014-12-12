def is_number(s):
    try:
        n=str(float(s))
        if n == "nan" or n=="inf" or n=="-inf" : return False
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False
    return True


tpl1=(1,2.2,3)
tpl2=('a','c','d')
tpl3=tpl1+tpl2
for var in tpl3:
	if is_number(var):
		print var, '-Integer'
	else:
		print var, '-Non Integer'
