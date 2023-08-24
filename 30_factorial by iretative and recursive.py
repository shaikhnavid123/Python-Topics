# n! = n * n-1 * n-2 * n-3 ........ 1
# n! = n * (n-1)!

print("Iterative Factorial Method :")
def factorial_iterative(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3 ........ 1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
# print(factorial_iterative(5))
number = int(input("Enter a number:"))
print(factorial_iterative(number))

print("Recursive Factorial Method :")
def factorial_recursive(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial_recursive(n-1)
number1 = int(input("Enter a number:"))
print(factorial_recursive(number1))


#Fibonachi numbers : 0 1 1 2 3 5 8 13 21 ....
print("Fibonachi numbers :")
def fibonacci_number(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

num3 = int(input("Enter a number :"))
print(fibonacci_number(num3))
