list1 = ["Elliot", "Alderson", "Mr.Robot", "Zenox"]
list2 = [["Elliot", 2], ["Alderson", 9], ["Mr.Robot", 5], ["Zenox", 3]]
dict1 = dict(list2)

#print(dict1)
#print(list1[0], list1[1])

#for item in list1:
#    print(item)
#for item, achivements in list2:
#    print(item, achivements)
#    print(item, "Achivements are", achivements)
#for item, achivements in dict1.items():
#    print(item, "achivements are", achivements)

items = [int, float, "Elliot", 1, 5, 9, 5, 3, 4, 3, 6, 7, 8]

for item in items:
    if str(item).isnumeric() and item<5:
        print(item)
