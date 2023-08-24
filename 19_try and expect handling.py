num1 = input("Enter a number :")
num2 = input("Enter a number :")

try:
    print("Sum of these two numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is a very important line")

