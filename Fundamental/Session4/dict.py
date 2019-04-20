code = {
    "gg": "good game",
    "ez": "easy",
    "tyvm": "thank you very much",
}
for key in code.keys():
    print(key)
loop = True
while loop:    
    x = input("what do you want? ")
    if x in code:
        print(code[x])   
    elif x == "end":
        loop = False
    else:
        a = input("Do you wanna add this to our dictionary? (Y/N) ").upper()
        if a == "Y":
            b = input("Repeat it again please? ")  
            c = input("What does it mean? ")
            code[b] = c
            print(code)
        else:
            print("Alright, let's go back")    