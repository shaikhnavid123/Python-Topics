#s = set()

s = set()
print(type(s))

l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
#print(type(s_from_list))

s.add(1)
s.add(1) #set function is used to add unique values, and same values can't be printed
print(s)

s.add(1)
s.add(2)
#s.add(3)
print(s)

#s.remove(3)
#print(s)

s.union({1, 2,})
print(s)

s.union({1, 2, 3})
print(s)

s1 = s.union({1, 2, 3})
print(s, s1)

s1 = s.intersection({1, 2, 3})
print(s, s1)

s1 = s.difference({1, 2, 3})
print(s, s1)

