from os import strerror
try:
	bf = open('file.bin', 'rb')
	data = bytearray(bf.read())
	bf.close()
	for b in data:
		print(hex(b), end=' ')
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))