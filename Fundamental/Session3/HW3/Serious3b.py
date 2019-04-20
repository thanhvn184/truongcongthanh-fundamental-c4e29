print('''
Let's play a game
All you have to do is guess the word that had been scramble
If you don't want to play anymore, just type "endgame"
Let's go!
''')
list0 = ["undead", "knight", "nagasiren", "demonhunter"]
import random
loop = True
while loop:
        i=random.choice(list0)
        x = list(i)
        random.shuffle(x)
        print(x)
    while loop:
        a = str(input("Your guess is: "))
        if a==i:
            print("Hurray!")
        elif a==("endgame"):
            loop = False
            print("Done")    
        else:
            print("Wrong, try more!")    