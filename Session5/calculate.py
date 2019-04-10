
def calc(x, y, op_choice):
    result = 0
    if op_choice == "+":
        result = x + y
    elif op_choice == "-":
        result = x - y
    elif op_choice == "*":
        result = x * y
    elif op_choice == "/":
        result = x / y

    return result 

