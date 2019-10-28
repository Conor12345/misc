f = open("input.txt", "r")
list1 = []
for line in f:
    list1.append(line.strip())

#list1 = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

list2 = []
for i in list1:
    dict1 = {}
    for j in i:
        if j in dict1:
            dict1[j] += 1
        else:
            dict1[j] = 1
    list2.append(dict1)

twocount = 0
threecount = 0
for dict2 in list2:
    twos = False
    threes = False
    for i in dict2:
        if dict2[i] == 2 and twos == False:
            twocount += 1
            twos = True
        elif dict2[i] == 3 and threes == False:
            threecount += 1
            threes = True

print(twocount * threecount)