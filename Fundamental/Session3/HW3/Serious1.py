in4 = input("Welcome to our club, what do you want (C, R, U, D)? ").upper()
menu = ["Heiniken", "Whiskey", "Cocktail"]
if in4 == ("R"):
    print("We have: ", *menu, sep="-")
elif in4 == ("C"):
    create = input("Your new drink is: ")
    print(create)
    menu.append(create)    
    print("We have: ", *menu, sep="-")
elif in4 == ("U"):
    update1 = int(input("Update position? "))
    update2 = input("Your new drink is? ")
    menu[update1 - 1] = update2
    print("We have: ", *menu, sep="-")
elif in4 == ("D"):
    delete = int(input("Delete position? "))
    del menu[delete - 1]
    print("We have: ", *menu, sep="-")
else:
    print("Please use C, R, U or D to run program.")    
