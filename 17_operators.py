#Types of Operators :
#1 - Arithmetic Operators
#2 - Assignment Operators
#3 - Comparison Operators
#4 - Logical Operators
#5 - Identity Operators
#6 - Membership Operators
#7 - Bitwise Operators

################################################################################
"""
#1 - Arithmetic Operators :
print("Arithmetic Operators :")
print("5 + 6 is", 5+6)
print("5 - 6 is", 5-6)
print("5 * 6 is", 5*6)
print("5 / 6 is", 5/6)
print("5 % 6 is", 5%5) #reminder
print("5 % 3 is", 5%3) #also known as modulus operators
print("5 ** 6 is", 5**6) #race to the power
print("5 ** 3 is", 5**3) #cube root
print("5 // 6 is", 5//6) #gives a number in nearest integer
print("15 // 6 is", 15//6)

################################################################################

#2 - Assignment Operators :
print("Assignment Operators :")
x = 5
print(x)
x +=7
#x -=7
#x /=7
#x *=7
#x %=7 (x = x%7)
print(x)

################################################################################

#3 - Comparison Operators :
print("Comparison Operators :")
i = 5
print(i == 8)
print(i == 5)
print(i != 5)
print(i < 8)
print(i > 8)
print(i > 5)
print(i >= 5)

################################################################################

#4 - Logical Operators : (aka Boolean Algebra/mathematical logic)
print("Logical Operators :")
a = True
b = False
print(a and a)
print(a and b)
print(a or b)
print(a is b)
print(a is not b)

################################################################################

#5 - Identity Operators :
print("Identity Operators :")
a = 5
b = 6
print(a is not b)
print(a is b)
#print(5 is not 5) - False
#print(6 is not 5) - True
print(6 != 5)

################################################################################

#6 - Membership Operators :
print("Membership Operators :")
list = [3, 5, 3, 56, 9, 12, 23]
print(3 in list)
print(8 in list)
print(3 not in list)
print(4 not in list)


################################################################################
"""
#7 - Bitwise Operators :
print("Bitwise Operators :")

#Binary codes :
#0 = 00
#1 = 01
#2 = 10
#3 = 11

print(0 and 1)
print(1 & 3)
print(0 or 3)
print(1 | 0)

