f = open("input.txt", "r")

nums = 0
for line in f:
    nums += int(line.strip())

print(nums)