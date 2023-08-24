#-------------------------------MAP-----------------------------------------------------#
# num1 = ["3", "5", "12"]
# num1 = list(map(int, num1))
# num1[1] = num1[1] + 2
# print(num1[1])

# for i in range(len(num1)):
#     num1[i] = int(num1[i])
# num1[1] = num1[1] + 2
# print(num1[1])

# def sq(a):
#     return a*a
# num2 = [2,4,5,2,6,5,7,8,9,6]
# square = list(map(sq, num2))
# # square = list(map(lambda x:x*x, num2))
# print(square)
#
# cube = list(map(lambda x:x*x*x, num2))
# print(cube)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square, cube]
#
# for i in range(5):
#     value = list(map(lambda x:x(i), func))
#     print(value)

#-------------------------------FILTER-----------------------------------------------------#
# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(n):
#     return n>5

# gr_than = list(filter(is_greater_5, list_1))
# print(gr_than)

#-------------------------------REDUCE-----------------------------------------------------#
from functools import reduce
list2 = [1,2,3,4]

# num = 0
# for i in list2:
#     num = num + i
# print(num)

num = reduce(lambda x,y:x+y, list2)
print(num)

