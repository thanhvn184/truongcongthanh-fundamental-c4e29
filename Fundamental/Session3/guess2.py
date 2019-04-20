# loop = True
# print("Is 51 your number?")

# while loop:

#     A=input("Your answer is: ")
#     if A == "s":
#         from random import *
#         x=randint(0, n)
#         print("Is", x, "your number?")
#     elif A == "b":
#         from random import *
#         x=randint(n, 100)   
#         print("Is", x, "your number?")
#     elif A == "c":
#         print("EZ")  
#         loop=False


low = 0
high = 100
loop = True
while loop:
    mid = (low+high)//2
    A = input("Is {} your number? ".format(mid))
    if A == "c":
        print("Bingo")
        loop = False
    elif A == "s":
        high = mid
    elif A == "b":
        low = mid   



