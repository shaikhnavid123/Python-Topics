l = 10 #Global Variable
def function1(n):
    # l = 5 #Local variable
    m = 8
    global l
    l = l + 45
    print(l)
    # print(l, m)
    print(n, "I have printed")
function1("This is me")
# print()

x = 89
def elliot():
    x = 20
    def rami():
        global x #global keyword can only change variable direct outside of function not the upper function
        x = 88
    print('Before calling elliot()', x)
    rami()
    print("After calling elliot()", x)
elliot()
print(x)
