# f1 = open("Rohan Exercise.txt")

try:
    f2 = open("doeqs.txt")

# except Exception as e:
#     print(e)

except EOFError as e:
    print("EOF Error has been conducted", e)

except IOError as e:
    print("IO error has been conducted", e)

else:
    print("This will only run if except is not running")

finally:
    print("Run this anyway...")
    # f.close()

print("Important Stuff")