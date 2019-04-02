size0 = [10, 23, 69, 184, 207, 430, 300]
print('Hello my name is Thanh and these are my sheep sizes: ')
print(size0)
print("Now my biggest ship has size", max(size0), "let's shear it")
size0[size0.index(max(size0))] = 8
print("After shearing, here is my flock: ")
print(size0)
for j in range(4):
    print("MONTH", j+1)
    print("1 month has passed, now here is my flock: ")
    size0 = [i+50 for i in (size0)]
    print(size0)
    print("Now my biggest ship has size", max(size0), "let's shear it")
    size0[size0.index(max(size0))] = 8
    print("After shearing, here is my flock: ")
    print(size0)
tong = 0
for x in size0:
    tong = tong + x
print("My flock has size in total: ", tong)
print("I would get: ", tong, "* 2$ =", tong*2,"$")