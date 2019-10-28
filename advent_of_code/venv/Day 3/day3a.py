f = open("input.txt", "r")
list1 = []
for line in f:
    list1.append(line.strip())

#list1 = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

def printB(board):
    for i in board:
        print(i)

board = []
for i in range(1200):
    list2 = []
    for j in range(1200):
        list2.append([])
    board.append(list2)

printB(board)

for i in list1:
    i2 = i.split(" ")
    print(i2)
    wh = i2[-1].split("x")
    width = wh[0]
    height = wh[1]
    xyspacing = ((i2[-2])[:-1]).split(",")
    xspace = xyspacing[0]
    yspace = xyspacing[1]
    print(xspace, yspace, width, height)
    for w in range(int(width)):
        for h in range(int(height)):
            board[int(yspace) + h][int(xspace) + w].append(1)

printB(board)

count = 0
for i in board:
    for j in i:
        if len(j) > 1:
            count += 1

print(count)