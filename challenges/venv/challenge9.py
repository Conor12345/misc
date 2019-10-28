def printScores():
    list1 = [55, 63, 27, 74, 44]
    for i in list1:
        print(addBonus(i))

def addBonus(score):
    if score < 30:
        return score
    elif score < 50:
        return score + 1
    elif score < 70:
        return score + 3
    else:
        return score + 5

printScores()