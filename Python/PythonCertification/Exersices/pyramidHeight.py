blocks = int(input("Enter number of blocks: "))
height = 0
inlayer = 1

# while blocks > 0:
#     height += 1
#     blocks -= height

#     if blocks < 0:
#         height -= 1
#         break

while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1

print(height)
