str1 = "abcdefghijklmnopqrstuvwxyz"

for i in range(0, 26):
        foo = str1[i:10]
        if foo == "":
            break
        print(foo)

