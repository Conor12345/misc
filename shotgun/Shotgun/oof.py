import shotfun


list1 = []
for i in range(100):
    list1.append(shotfun.s_ranint(0, 10))

print(list(set(list1)))