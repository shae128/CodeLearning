from random import randint

nums = []
for n in range(18):
    nums.append(randint(1, 5))

print(nums)

for num in set(nums):  # set function removes duplicates and sorts a list
    count = nums.count(num)
    print(f"There are {count} '{num}' in the list")
