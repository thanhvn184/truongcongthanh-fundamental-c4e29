from turtle import *
shape("turtle")
speed(0)

length=0
for i in range(10,200,5):
    forward(length)
    left(90)
    length += 5
mainloop()