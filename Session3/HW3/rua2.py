from turtle import *
mau = ["red", "blue", "brown", "yellow", "gray"]
for i in range(5):
    begin_fill()
    color(mau[i])
    for j in range(2):
        fd(50)
        lt(90)
        fd(100)
        lt(90)
    fd(50)
    end_fill()
mainloop()