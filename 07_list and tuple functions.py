#LISTING
#list = []
accessory = ["Mouse", "Keyboard", "Sound", "camera", 25]
print(accessory)
print(accessory[2])

#list slicing
print(accessory[0:])
print(accessory[:5])
print(accessory[:])
print(accessory[1:3])
print(accessory[::-1])

#list functions
numbers = [2, 9, 16, 1, 5]
numbers.append(35)
numbers.remove(9)
#numbers.pop() --- used for removing last value
numbers[1] = 55
print(numbers)
print(numbers[::-1])
print(numbers[2])
print(len(numbers))
print(max(numbers))
print(min(numbers))

numbers1 = [2, 9, 16, 1, 5]
numbers1.sort()
print(numbers1)


numbers2 = [2, 9, 16, 1, 5]
numbers2.reverse()
print(numbers2)

"""
mutable - can be change (LIST)
immutable - cannot be change (TUPPLES)
"""

#TUPLES
#tuple = ()
tp = (1, 4, 3)
print(tp)

a = 1
b = 5
a, b = b, a
"""
temp = a
a = b
b = temp
"""
print(a, b)

tp1 = (1)
print(tp1)

tp2 = (1,)
print(tp2)









