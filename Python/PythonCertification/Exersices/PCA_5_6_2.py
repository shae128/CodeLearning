def reciprocal(n):
	try:
		n = 1 / n
	except ZeroDivisionError:
		print("Division failed")
		n = None
	else:
		print("Everything went fine")
	finally:
		print("It's time to say good bye")
		return n

print(reciprocal(2))
print(reciprocal(0))