"""It shows the number grater than ^ in the list"""
list1 = ('car', 'bike', 43, 'scooter', 52, 5, 2, 'motorcycle', 44)
for items in list1:
    Type = type(items)
    if Type == int and items > 6:
        print(items)
