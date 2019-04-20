number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
op = ["+", "-", "*", "/"]
from random import *
from calculate import calc
x = choice(number)
y = choice(number)
op_choice = choice(op)

result = calc(x, y, op_choice)

error = choice([-1, 0, 1])
output = result + error
print("{0} {1} {2} = {3}".format(x, op_choice, y, output))
a = input("Your answer is(Y/N)? ").upper()
if error == 0:
    if a == "Y":
        print("Hura")
    elif a == "N":
        print("Wrong")   
else:
    if a == "Y":
        print("Wrong")
    elif a == "N":
        print("Hura")







