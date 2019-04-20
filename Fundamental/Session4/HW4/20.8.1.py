    
string = input("PLease enter your phrase: ")
string_lower = string.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for key in alphabet:
    if string_lower.count(key) != 0:
        print(key, string_lower.count(key))