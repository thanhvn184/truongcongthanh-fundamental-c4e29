from turtle import *
def draw_square(length, colors):
    color(colors)
    for i in range(4):
        fd(length)
        lt(90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()

# from turtle import *
# def draw_star(x, y, length):
#     penup()
#     setx(x)
#     sety(y)
#     pendown()
#     for i in range(5):
        
#         fd(length)
#         right(144)
# speed(0)
# color('blue')
# for i in range(100):
#     import random
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(3, 10)
#     draw_star(x, y, length)
# mainloop()




