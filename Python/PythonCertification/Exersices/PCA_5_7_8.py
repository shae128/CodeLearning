def PowersOf2(n):
	pow = 1
	for i in range(n):
		yield pow
		pow *= 2

for v in PowersOf2(8):
	print(v)