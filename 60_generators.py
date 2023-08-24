#iterable
#iterator
#iteration

# for i in range(25):
#     print(i)

def gen(n):
    for i in range(n):
        yield i

# g = gen(3487645334778766431334)
g = gen(3)
print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())

h = "harry"
ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

for c in h:
    print(c)

