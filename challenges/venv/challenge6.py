def printarray():
    print("Table is now: ")
    for row in range(2):  # assuming the rows are numbered 0 to 1
        for column in range(3):  # assuming the columns are 0 to 2
            print(hoorray[row][column], end=" ")  # see below
        print()

hoorray = [[0, 0, 0], [0, 0, 0]]
printarray()
for i in range(3):
    row = int(input("Row number: "))
    column = int(input("Column number: "))
    hoorray[row][column] = int(input("Number to input: "))
    printarray()

print("Row 1 total ", sum(hoorray[0]))
print("Row 2 total ", sum(hoorray[1]))
