from random import *
x=randint(0,100)
loop=True
while True:
    n=int(input("Guess my number: "))
    if n<x:
        print("Be qua")
    elif n>x:
        print("To qua")
    else:
        print("Dung roi")
        loop=False


