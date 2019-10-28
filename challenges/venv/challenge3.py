x = int(input("What is your score? "))

if x < 30:
    print("Grade E")
elif x < 45:
    print("Grade D")
elif x < 60:
    print("Grade C")
elif x < 80:
    print("Grade B")
else:
    print("Grade A")