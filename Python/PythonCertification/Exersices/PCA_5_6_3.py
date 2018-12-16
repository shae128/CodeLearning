try:
	i = int("hello!")
except Exception as e:
	print(e)
	print(e.__str__())