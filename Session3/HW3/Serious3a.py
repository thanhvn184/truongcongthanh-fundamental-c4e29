word = ["w", "a", "r", "r", "i", "o", "r"]
import random
loop = True
while loop:
    x = random.sample(word, 7)
    print(*x)
    a = input("Your answer is: ")
    if a == ("warrior"):
        print("Congrats!")
        loop = False
    else:
        print("Sorry but you have to try again :(")    