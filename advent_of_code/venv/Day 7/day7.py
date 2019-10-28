f = open("input.txt", "r")
inputlist = []
for line in f:
    inputlist.append((line[:-2]).split(" "))
print(inputlist)

instructions = ""
needs = []
setlist = []
for instruct in inputlist:
    list1 = []
    list1.append(instruct[1])
    list1.append(instruct[7])
    needs.append(list1)
    if instruct[1] not in setlist:
        setlist.append(instruct[1])
    if instruct[7] not in setlist:
        setlist.append(instruct[7])
setlist.sort()
print(needs,setlist)

while True:
    setlist2 = []
    for j in range(0, len(setlist2)-1):
        if i[0] == setlist2[j]:
            setlist.pop(j)
    setlist2.sort()
    instructions += setlist2[0]
    foo = []
    for i in setlist:
        if i not in instructions:
            foo.append(i)
    print(foo)
    break

