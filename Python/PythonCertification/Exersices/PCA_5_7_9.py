def PowersOf2(n):
	pow = 1
	for i in range(n):
		yield pow
		pow *= 2

t = [ x for x in PowersOf2(5) ]
print(t)