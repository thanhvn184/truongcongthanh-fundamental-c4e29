person = {
    "name": "Thanh",
    "age": 19,
    "uni": ["NEU"],
    "ex": 2,}


#  =>> key: value,

#  1. READ
# print(person)
# print(person["name"])
# print(person["age"])


#     loop by key
# for key in person.keys():
#     print(key)


#     loop by value
# for value in person.values():
#     print(value)


#     loop by item
# for key, value in person.items():
#     print(key, value)


#  2. CREATE or UPDATE
# person["ex"] = 5
# print(person)
uni = person["uni"]
uni.append("HMU")


#  3. DELETE
# del person["age"]
print(person)
