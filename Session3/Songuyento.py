# x = int(input("nhap so: "))
# loop = True
# while loop:
#     for i in range(2, x):
#         x = x%i
#         if x==0:
#             loop = False
#              print("Day khong la so nguyen to")
#         else:
#             loop = False
#                print("day la so nguyen to")     


#Cach-1
x = int(input("nhap so: "))
i = 2
loop=True
while i<x:
    if x%i==0:
        loop=False
    i += 1 
if loop == True:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")      




#Cach-2
x = int(input("nhap so: "))
i=2
loop=True
while loop:
    if n%i==0:
        loop=False
        print("Khong phai so nguyen to")    
    i += 1
    if i==n:
        loop=False
        print("Khong phai so nguyen to")        


