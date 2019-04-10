def get_even_list(l):
    for i in list(l):
        if i % 2 != 0:
            l.remove(i)
    return (l)        
l = [1, 2, 3, 4, 5] 



even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
