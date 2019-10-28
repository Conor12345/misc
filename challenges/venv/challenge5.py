sum = 0

while sum < 100:
    num1 = int(input("Enter a number: "))
    if num1 < 0:
        break
    sum += num1
print("The total is", sum)