list = [ 1 if x % 2 == 0 else 0 for x in range(10) ]
genr = ( 1 if x % 2 == 0 else 0 for x in range(10) )

for v in list:
	print(v, end=" ")
print()

for v in genr:
	print(v, end=" ")
print()