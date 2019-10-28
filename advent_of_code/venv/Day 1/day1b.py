f = open("input.txt", "r")

nums = []
for line in f:
    nums.append(int(line.strip()))

freqlist = []
count = 0
index = 0
attempts = 0

while True:
    count += nums[index]
    if (count in freqlist):
        print(count,"DONE")
        break
    else:
        freqlist.append(count)
    index += 1
    index = index % len(nums)
    attempts += 1
    print(attempts)