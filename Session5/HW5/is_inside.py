def is_inside(check=[], rectangle=[]):
    x1 = check[0]
    x2 = rectangle[0]
    y1 = check[1]
    y2 = rectangle[1]
    width = rectangle[2]
    height = rectangle[3]
    if x1 in range(x2, x2+width):
        if y1 in range(y2, y2+height):
            return True
        else:
            return False
    else:
        return False
test = is_inside([180, 120],[140, 60, 200, 100])
if test == True:
    print("true!!")
else:
    print("wrong!!")