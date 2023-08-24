# no. divisible by 3 : list comprehension
# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

# ls = [i for i in range(100) if i%3==0]
# print(ls)

#dictionary comprehension
# dict1 = {0:"item0", 1:"item1", 2:"item2"}
# print(dict1)

# dict1 = {i:f"item {i}" for i in range(100) if i%20==0}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1,"\n",dict2)
#
# dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}
# # dresses = [dress for dress in ["dress1", "dress2", "dress1", "dress2"]]
# print(dresses)
# print(type(dresses))

# evens = (i for i in range(100) if i%2==0)
# # print(evens)
# # print(type(evens))
# # for item in evens:
# #     print(item)


