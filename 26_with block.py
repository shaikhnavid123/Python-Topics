f = open("22_textfile")
print(f.readlines())
# print(f.readline())
f.close()

with open("22_textfile") as f:
    a = f.read()
    # a = f.read(5)
    print(a)

    