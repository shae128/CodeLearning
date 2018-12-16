cipher = input("Please Enter the code: ")

text = ''

for char in cipher:

    if not char.isalpha():
        text += char
        continue

    code = ord(char) - 1

    if code < ord("A"):
        code = ord("Z")

    text += chr(code)


print(text)
