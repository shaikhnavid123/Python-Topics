"""
i = 0
while (True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1, end=" ")
    if(i==44):
        break

    i = i+1
"""
#Q. Create a program in which, taking input from user until they'll not put number greater than 100

while (True):
    inp = int(input("Enter a number :\n"))
    if inp>100:
        print("Congrats! You've entered than 100\n")
        break
    else:
        print("Try again!\n")
        continue
