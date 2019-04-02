# fav = ["dota2", "watch movies", "badminton"]
# print(*fav, sep=",")
# add=input("anything else?")
# fav.append(add)
# print(fav)



fav = ["games", "watch movies", "badminton"]
for index, item in enumerate(fav):
    print(index+1, item, sep=".")  
    print("{}. {}".format(index+1, item))