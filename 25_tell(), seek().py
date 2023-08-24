f = open("22_textfile")

# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

# print(f.readline())
# f.seek(0)
# print(f.readline())

# print(f.readline())
# f.seek(11)
# print(f.readline())

f.seek(11)
print(f.tell())
print(f.readline())