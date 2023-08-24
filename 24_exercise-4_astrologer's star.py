"""Pattern Printing :
Input = Interger n
Boolean = True or False

True n=4
*
**
***
****

False n=5
****
***
**
*
"""

#Q. Take input from user in integer, and also take input of Boolean variable (0 and 1), this variable can
# be true or false, based on true of false print a star pattern row-wise, for true print ascending order stars,
# for false print descending order star

#SOLUTION-1:

print("Pattern Printing :")
num = int(input("Enter num of row you want :"))
print("Enter 1 or 0")
bool_var = input("1 for True or 0 for False :")
if bool_var=="1":
    for i in range(0, num, +1):
        print("*"*int(i))
if bool_var=="0":
    for i in range(num, 0, -1):
        print("*"*int(i))

#SOLUTION-2:
"""
n=int(input("Enter no. of row :"))
a=int(input("Enter a boolean no. :"))
if(bool(a)):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print()
else:
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print("*", end="")
        print()
"""