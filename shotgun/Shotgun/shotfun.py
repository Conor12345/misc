from random import *


def s_sort(listin):
    while not s_inorder(listin):
        s_shuffle(listin)
    return listin


def s_search(listin, target):
    found = False
    while not found:
        val = randint(0, len(listin)-1)
        if listin[val] == target:
            return val


def s_ranint(lower=int, upper=int):
    list1 = []
    for i in range(lower, upper + 1):
        list1.append(i)
    print(list1)


def s_shuffle(listin):
    return shuffle(listin)


def s_inorder(listin):
    for i in range(len(listin) - 1):
        if listin[i] > listin[i + 1]:
            return False
    return True

s_ranint(1, 10)