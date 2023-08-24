# a = input("What is your name?")
# print(f"Hello, {a}")
#
# b = input("Amount you want to invest:")
# print(f"Amount, {b}")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# if int(b)==0:
#     raise ZeroDivisionError("Zero can't be an input")

c = input("Enter your name :")
try:
    print("Thanks for checking,", c)
except Exception as e:
    if c == "elliot":
        raise ValueError("Elliot is block by this website")
    print("Exception handle")