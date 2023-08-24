def minus(a, b):
    return a-b
print(minus(5, 2))

add = lambda x, y: x+y
print(add(5, 9))

def add(x, y):
    return x+y
print(add(5, 8))

def a_first(a):
    return a[1]
    # return a[0]
a = [[1, 3], [1,2], [5,0]]
a.sort(key=a_first)
print(a)

b = [[2, 9], [1,2], [5,0]]
b.sort(key=lambda x:x[1])
print(b)