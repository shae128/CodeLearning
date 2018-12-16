from os import strerror
try: 
	stream = open("c:/users/user/Desktop/file.txt","rt")
	# actual processing goes here
	stream.close()
except Exception as exc:
	print("File could not be opened:",strerror(exc.errno));
