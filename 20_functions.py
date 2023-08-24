
#built in function :
a = 9
b = 6
c = sum((a, b)) #built in funtion : ctrl + hover/click on the function has been used to view more functions
print(c)

#user defined function
def function1():
    print("Hello you are in function1")
function1()
#print(function1())


def function2(a, b):
    """This function will calculate average of two numbers
    this function does not work for three numbers"""
    average = (a+b)/2
    #print(average)
    return average
#function2(5, 7)
v = function2(5, 7)
print(v)
print(function2.__doc__)