# so = int(input("Enter your number"))
# count = 0
# while so>0:
#     so = so // 10
#     count += 1
    
# print (count)



x = int(input("enter your number"))
count = 0
loop = True
while loop:
    x = x // 10
    count += 1
    if x == 0 :
        loop = False
print(count)