def function_name(*args01):
    print(type(args01))
    print(args01[2])
name = ["Angela", "Rami", "Daniel", "Alderson"]
function_name(*name)

def function_name01(normal, *args02, **kwargs01):
    for item in args02:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs01.items():
        print(f"{key} is a {value}")

name1 = ["Tyriel", "Elliot", "Darlin", "Robert"]
normal = "This are the legends that made a mission possible"
kw = {"Danny":"Programmer", "Mr.Robot":"Hacker", "Robert":"CTO"}
function_name01(normal, *name1, **kw)