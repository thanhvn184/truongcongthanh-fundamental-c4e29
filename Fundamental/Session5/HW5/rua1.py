# def hello_world():
#     for i in range(3):
#         print("hello_world")
# hello_world()        


# def sum(a, b):
#     print(a+b)
# sum(2, 6)    

from turtle import *
def draw_square(length, colors):
    color(colors)
    for i in range(4):
        fd(length)
        lt(90)
draw_square(100, "red")        
mainloop()






