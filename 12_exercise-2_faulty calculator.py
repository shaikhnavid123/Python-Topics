#Q. Design a calculator which will correctly solve all the problems expect the following ones :
#45 * 3 = 555, 56+9 = 77, 56/6 = 4
#Your program should take operator and the two numbers as input from the user and then return the result

#FAULTY CALCULATOR :
#Solution : 03
print("Choose operators : +, *, /")
n = input()
print(n)
if(n=="+"):
    a = int(input("enter 1st number :"))
    b = int(input("enter 2nd number :"))
    if (a==56 and b==9):
        print("addition is", 77)
    else:
        print("addition is", a+b)

elif(n=="*"):
    a = int(input("enter 1st number :"))
    b = int(input("enter 2nd number :"))
    if (a==45 and b==3):
        print("multiplication is", 555)
    else:
        print("addition is", a*b)

elif(n=="/"):
    a = int(input("enter 1st number :"))
    b = int(input("enter 2nd number :"))
    if (a==56 and b==6):
        print("division is", 4)
    else:
        print("division is", a/b)



"""
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
cal_type = int(input("+, -, *, /"))
print("your answer is :", num1, cal_type, num2)
"""
"""
print("Enter first number :")
num1 = int(input())
print("Enter second number :")
num2 = int(input())
print("So what you want?"+"+,-,*,/")
num3 = input()
"""
"""
first_num = int(input("enter first number :"))
second_num = int(input("enter second number :"))
operator = input(input("enter operator :"))
if first_num==45 and second_num==3 and operator=="*":
    print("555")
elif first_num==56 and second_num==9 and operator=="+":
    print("777")
elif first_num==56 and second_num==6 and operator=="/":
    print("4")
else:
    print(first_num+operator+second_num)
"""
