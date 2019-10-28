import itertoolsv == 4:
                failed = True
                break
        if listFront[i] == 4:
            if listBack[i] == 7:
                failed == True
                break

    # Comet and Vixen in the same column - 4 and 5 in the same column of 4
    if (4 in listFront and 5 in listFront) or (4 in listBack and 5 in listBack):
        print("oof")
    else:
        failed == True

    listy = listFront + listBack
    print(listy)

    if failed:
        masterlist2.append(listy)

    print(listFront, listBack, failed)
print(masterlist2, len(masterlist2))