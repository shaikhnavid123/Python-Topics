class A:
    def met(self):
        print("This is method from a class A")

class B(A):
    def met(self):
        print("This is method from a class B")

class C(A):
    def met(self):
        print("This is method from a class C")

class D(B, C):
    def met(self):
        print("This is method from a class D")

a = A()
b = B()
c = C()
d = D()

d.met()
