import math
me = "Elliot"
a1 = 5
a = "This is %s %s"%(me, a1)
print(a)

b = "This is {} {}"
c = b.format(me, a1)
print(c)

d = f"This is {me} {a1} {6+1} {math.cos(0)}"
print(d)
