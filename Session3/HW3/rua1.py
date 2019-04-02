from turtle import *
mau = ["red", "blue", "brown", "yellow", "gray"]
goc = [120, 90, 72, 60, 360/7]
for i in range(5):
    color(mau[i])
    for j in range(1,i+4):
        fd(100)
        lt(goc[i])
mainloop()