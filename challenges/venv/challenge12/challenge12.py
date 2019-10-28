while True:
    f = open("storage.txt", "r")
    for line in f.readlines():
        print(line.strip())

    f = open("storage.txt", "a")
    f.write("\n" + input("Name: ") + " - " + str(int(input("Score:"))))

    f.close()