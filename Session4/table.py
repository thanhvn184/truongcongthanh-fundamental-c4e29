Hai = {
    "Ten": "Hai",
    "Luong": 50000,
    "Ngay": 25,
    "Gio/Ngay": 8,
}
Duc = {
    "Ten": "Duc",
    "Luong": 25000,
    "Ngay": 20,
    "Gio/Ngay": 6,
} 
Minh = {
    "Ten": "Minh",
    "Luong": 20000,
    "Ngay": 27,
    "Gio/Ngay": 5,
}
Long = {
    "Ten": "Long",
    "Luong": 15000,
    "Ngay": 30,
    "Gio/Ngay": 3,
}
list0 = [Hai, Duc, Minh, Long]


for i in list0:
    




        total = 0
        salary=(i["Luong"])*(i["Ngay"])*(i["Gio/Ngay"])
        total += salary
print(total)        
  

