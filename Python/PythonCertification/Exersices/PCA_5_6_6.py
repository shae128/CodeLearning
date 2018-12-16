class MyZeroDivisionError(ZeroDivisionError):
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("worse news")
	else:		
		raise ZeroDivisionError("bad news")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('Division by zero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')		