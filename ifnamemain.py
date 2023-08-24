def printelliot(str):
    return f"Mi nombre es {str}"

def add(num1, num2):
    return num1 + num2
print(add(5, 4))

print("and the name is", __name__)
if __name__ == '__main__':
    print(printelliot("Elliot"))
    o = add(4, 3)
    print(o)
