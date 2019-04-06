loop = True
while loop:
    print("Answer the following question: ")
    print("If x = 8, then what is the value of 4(x + 3) ?")

    answer = {
        "1." : 35,
        "2." : 36,
        "3." : 40,
        "4." : 44,
    }
    for item in answer.items():
        print(item)
        
    x = int(input("Your choice is? "))
    if x == 4:
        print('Bingo')
        loop = False
    elif x != 4:
        print(':(') 